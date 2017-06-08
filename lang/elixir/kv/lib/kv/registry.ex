defmodule KV.Registry do

	use GenServer

	## Client API

	@doc """
	Starts the registry with the given `name`.
	"""
	def start_link(name) do
    # 1. Pass the name to GenServer's init
		GenServer.start_link(__MODULE__, name, name: name)
	end

	@doc """
	Looks up the bucket pid for `name` stored in `server`.

	Returns `{:ok, pid}` if the bucket exists, `:error` otherwise.
	"""
	def lookup(server, name) when is_atom(server) do
    # 2. Lookup is now done directly in ETS, without access server
    case :ets.lookup(server, name) do
      [{^name, pid}] -> {:ok, pid}
      [] -> :error
    end

    # Accessing w/out ETS
    # GenServer.call(server, {:lookup, name})
	end

	@doc """
	Ensures there is a bucket associated to the given `name` in `server`.
	"""
	def create(server, name) do
		GenServer.cast(server, {:create, name})
	end

	## Server Callbacks

	def init(table) do

    # 3. We have replace the names map by the ETS table
    names = :ets.new(table, [:named_table, read_concurrency: true])

    refs  = %{}

		{:ok, {names, refs}}
	end

  # 4. The previous handle_call callback for lookup was removed

	def handle_cast({:create, name}, {names, refs}) do

    # 5. Read and write to the ETS table instead of the map
    case lookup(names, name) do
      {:ok, _pid} -> 
        {:noreply, {names, refs}}
      :error ->
        {:ok, pid} = KV.Bucket.Supervisor.start_bucket
        ref = Process.monitor(pid)
        refs = Map.put(refs, ref, name)
        :ets.insert(names, {name, pid})
        {:noreply, {names, refs}}
		end
	end

  def handle_info({:DOWN, ref, :process, _pid, _reason}, {names, refs}) do

    # 6. Delete from the ETS table instead of the map
    {name, refs} = Map.pop(refs, ref)
    :ets.delete(names, name)
    {:noreply, {names, refs}}
  end

  @doc """
  catch-all clause to discard any unknown message
  """
  def handl_info(_msg, state) do
    {:noreply, state}
  end
end

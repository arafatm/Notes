defmodule KV.Supervisor do
  use Supervisor

  def start_link do
    Supervisor.start_link(__MODULE__, :ok) # name the process so we can refer w/out PID
  end

  def init(:ok) do
    children = [
      worker(KV.Registry, [KV.Registry]), # will start KV.Registry.start_link(KV.Registr)
      supervisor(KV.Bucket.Supervisor, [])
    ]

    # :one_for_one => only restart this child
    supervise(children, strategy: :rest_for_one)
  end
end

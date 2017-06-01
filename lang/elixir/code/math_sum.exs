defmodule Math do
  def sum_list([head | tail], accumulator) do
    IO.puts "sum: [#{head}, #{Enum.join(tail, ", ")}] #{accumulator}"
    sum_list(tail, head + accumulator)
  end

  def sum_list([], accumulator) do
    IO.puts "accumulator: #{accumulator}"
    accumulator
  end
end

Math.sum_list([1, 2, 3], 4) #=> 6



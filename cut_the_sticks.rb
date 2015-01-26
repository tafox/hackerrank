#!/usr/bin/env ruby

n = gets.chomp.to_i
sticks = gets.split(" ")
sticks = sticks.map(&:to_i)

while !sticks.empty? do
    min = sticks[0]
    for i in 0...sticks.length do
        if min > sticks[i]
            min = sticks[i]
        end
    end
    sticks_cut = 0
    i = 0
    while i < sticks.length do
        sticks[i] -= min
        sticks_cut += 1
        if sticks[i] <= 0
            sticks.delete_at(i)
            i -= 1
        end
        i += 1
    end
    puts sticks_cut
end

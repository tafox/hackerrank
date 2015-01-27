#!/usr/bin/env ruby

def  lonelyinteger( a)
    c = Array.new(101)
    for i in 0...101
        c[i] = 0
    end
    for i in 0...a.length
        c[a[i]] += 1
    end
    for i in 0...c.length
        if c[i] == 1
            return i
        end
    end
end

a = gets.strip.to_i
b = gets.strip.split(" ").map! {|i| i.to_i}
print lonelyinteger(b)

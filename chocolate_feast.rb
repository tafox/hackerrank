t = gets.to_i
	t.times{
		(n, c, m) = gets.split.map{|i| i.to_i}
		
		answer = 0
		wrappers = n/c
		answer = wrappers
		while m <= wrappers
			wrappers -= m
			answer += 1
			wrappers += 1
		end
		puts answer
	}

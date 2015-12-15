require 'date'
vals = []
input = "a"
while(!input.empty?)
	input = gets.chomp.gsub(/[\s\-#{"\.\/"}]/,'|').split('|')
	break if input.empty? 
	case input[0].length
	when 4
		input[1] = "%02d" % input[1] 
		input[2] = "%02d" % input[2]
		input = input.join
		date = Date.strptime(input, "%Y%m%d")
	when 1..2
		input[0] = "%02d" % input[0] 
		input[1] = "%02d" % input[1] 
		input[2] = "20%02d" % input[2] if input[2].length == 2
		input = input.join
		date = Date.strptime(input, "%m%d%Y")
	else
		date = "Invalid date"
	end
	vals << date.to_s
end
vals.each do |i|
	puts i
end
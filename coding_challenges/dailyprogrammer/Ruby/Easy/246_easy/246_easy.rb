#
# /r/dailyprogrammer Challenge #246 [Easy] 
#          X-mass lights            
# 										   
# Short Summary: Develop a program capable of deducing various details based on 
# 				 electricity laws/rules (see full problem for more details)	   
# 										   
# Full Problem: https://www.reddit.com/r/dailyprogrammer/comments/3xpgj8/20151221_challenge_246_easy_xmass_lights/
#  

def draw_circuit(i, s) 
	if(i>5)
		s.empty? ? draw_circuit(i-5, s+"*--|>|---|>|---|>|---|>|---|>|--*\n |                             |\n") : draw_circuit(i-5, s+" --|>|---|>|---|>|---|>|---|>|-- \n |                             |\n")
	elsif(i>0&&i<=5)
		s.empty? ? draw_circuit(0, s+"*-"+("-|>|--"*i)+("-----"*(5-i))+"*\n") : 
		draw_circuit(0, s+" -"+("-|>|--"*i)+("-----"*(5-i))+" \n")
	else s
	end
end

def leds(i)
	(1200 / i.to_f / 20 * 5).to_i
end

def part4(v1, mA, v2, mAh, h)
	leds = (mAh / h.to_f / mA * 5).to_i
	ohms = (h * 0.5 / 1.2).round(3)
	puts "Resistor: #{ohms}\nScheme:"
	puts draw_circuit(leds, "")
end

puts "Part 1"
File.open("246_easy_input1.txt", "r").readlines.each do |line|
	puts leds(line.to_f)
end
puts

puts "Part 2"
File.open("246_easy_input2.txt", "r").readlines.each do |line|
	puts draw_circuit(leds(line.to_f), "")
end
puts

puts "Part 3"
File.open("246_easy_input3.txt", "r").readlines.each do |line|
	puts (line.to_f * 0.5 / 1.2).round(3)
end
puts

puts "Part 4"
File.open("246_easy_input4.txt", "r").readlines.each do |line|
	l = line.split(' ').map{|n| n.to_f}
	part4(l[0], l[1], l[2], l[3], l[4])
end


#
# /r/dailyprogrammer Challenge #245 [Easy] 
#             Date Dilemma                 
# 										   
# Short Summary: Write a prorgam capable of converting any date format into the standard YYYY-MM-DD format.
#   (i.e. 3/2/15 => 2015/03/02)			   
# 										   
# Full Problem: https://www.reddit.com/r/dailyprogrammer/comments/3wshp7/20151214_challenge_245_easy_date_dilemma/
#  										   

# RegExs used
# MM/DD/YY(YY) 		=> /^(\d{1,2})[\/\s\.-](\d{1,2})[\/\s\.-](\d{4}|\d{2})$/
# YYYY/MM/DD 		=> /^(\d{4})[\/\s\.-](\d{1,2})[\/\s\.-](\d{1,2})$/
# tomorrow			=> /^tomorrow$/
# yesterday 		=> /^yesterday$/
# (num) (type) ago	=> /^(\d{1,}|last|next)\s(day|week|month|year)\sago(from\s[today|tomorrow|yesterday])?$/
# 

require 'date'
File.open("245_easy_input.txt", "r").readlines.each do |line|
	if !(v = line.match(/^(\d{1,2})[\/\s\.-](\d{1,2})[\/\s\.-](\d{4}|\d{2})$/)).nil?
		puts( (v[3].to_s.length==2 ? "20%02d"%v[3].to_s : v[3].to_s) + "-" + ("%02d"%v[1].to_s) + "-" + ("%02d"%v[2].to_s) )
	elsif !(v = line.match(/^(\d{4})[\/\s\.-](\d{1,2})[\/\s\.-](\d{1,2})$/)).nil?
		puts( v[1].to_s + "-" + ("%02d"%v[2].to_s) + "-" + ("%02d"%v[3].to_s) )
	else
		puts "invalid"
	end
end

# My old, way more robust version is below
# please don't judge me :'(

=begin
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
=end

############################################
# /r/dailyprogrammer Challenge #245 [Easy] #
#             Date Dilemma                 #
# 										   #
# Short Summary: Write a program capable   #
#   of converting any date format into the #
#   standard YYYY-MM-DD format.			   #
#   (i.e. 3/2/15 => 2015/03/02)			   #
# 										   #
# Full Problem: https://www.reddit.com/r/dailyprogrammer/comments/3wshp7/20151214_challenge_245_easy_date_dilemma/
#  										   #
############################################

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
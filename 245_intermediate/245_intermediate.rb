#
# /r/dailyprogrammer Challenge #245 [Intermediate] 
#          Ggggggg gggg Ggggg-ggggg!               
# 										   
# Short Summary: Write a program that can encode (whilst providing the key used) and decode 
# (given a provided key) strings into a series of G's and g's 		   
# 										   
# Full Problem: https://www.reddit.com/r/dailyprogrammer/comments/3x3hqa/20151216_challenge_245_intermediate_ggggggg_gggg/
#  										   

# RegExs used:
# Any of the defined Gg strings		=> /#{kv.values.join('|')}|[^Gg]/
# All unique strings				=> /#{uc.join('|')}/

def decode
	l = File.open("245_intermediate_encode_input.txt", "r").readlines
	kv = Hash[*l[0].split(' ').flatten(1)]
	s, res, ind, stop = l[1], "", 0, true
	while(!s.match(/#{kv.values.join('|')}|[^Gg]/).to_s.empty?)
		kv.each do |k,v|
			if (s[0]=~/[Gg]/).nil? || s[0]==" "
				return puts res if s.empty?
				res+=s[0] and ind+=1 and s=s[1,s.length]
				next
			end
			next if s.index(v).nil? || !s.index(v).zero?
			res+=k and s.slice!(0,v.length) and ind+=1
		end
	end
	puts res
end

def encode
	l = File.open("245_intermediate_encode_input.txt", "r").readlines[0]
	uc = l.gsub(/[^\w]/, '').split(//).uniq
	kv = uc.zip((0...uc.count).map{|i| ("%0#{Math.log(uc.count, 2).ceil}d" %i.to_s(2)).gsub(/[01]/, '0'=>'g', '1'=>"G")}.compact).to_h
	kv.each do |k,v| 
		print k + " " + v + " "
	end
	puts ""
	puts l.gsub(/#{uc.join('|')}/, kv)
end

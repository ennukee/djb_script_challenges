def decode(s, i)
	puts "s: #{s}"
	puts "i: #{i}"
	return i if s.nil? || s.empty?
	l = File.open("letter_hash.txt", "r").readline
	conv = Hash[*l.split(' ').flatten(1)].invert
	[] + 
		[(decode( s[2..-1], i+conv[s[0,2].to_i.to_s] ) if(s[0,2].to_i<27&&s[0,2].to_i>0))] + 
		[(decode(s[1..-1], i+conv[s[0]]) if s[0].to_i>0)]
end
#decode("1234", "").flatten.uniq.each {|i| puts i}
#decode("1234567899876543210", "").flatten.uniq.each {|i| puts i}

words = File.open("enable1.txt", "r").readlines
#decode("1321205", "").flatten.uniq.each {|i| puts i if i=~/[#{words.join('|')}]*/}
#decode("1252020518", "").flatten.uniq.each {|i| puts i if i=~/[#{words.join('|')}]*/}
#decode("85121215231518124", "").flatten.uniq.each {|i| puts i if i=~/[#{words.join('|')}]*/}

decode("81161625815129412519419122516181571811313518", "").flatten.uniq.each {|i| puts i if i=~/[#{words.join('|')}]*/}
def fac(i) (1..i).inject(:*) || 1 end
def comb(i, q) fac(i) / (fac(q)*fac(i-q)) end

def pc(l, w)
	#return 1 if [l,w].min == 0
	r = 0
	(0..[l,w].min).each do |k|
		#r += comb((l+w-k), l) * comb(l, k)
		r += comb(l, k) * comb(w, k) * (2**k)
	end
	r
end

def solve(file_name)
	words = File.open(file_name, "r").readlines
	l, w = words[0].split(', ').map{|v| v.to_i}
	grid = words[1..w].join.gsub(/[^X\.]/,'')
	x_i = ((0...grid.length).find_all{|v| grid[v,1]=='X'}).reverse
	puts x_i
	puts
	r = 1 and (0...x_i.length-1).each do |i|
		r *= pc(x_i[i]/l - x_i[i+1]/l, x_i[i]%l - x_i[i+1]%l)
		print pc(x_i[i]/l - x_i[i+1]/l, x_i[i]%l - x_i[i+1]%l)
		print " "
		print x_i[i]/l - x_i[i+1]/l
		print " "
		print x_i[i]%l - x_i[i+1]%l
		puts
		#puts "<INVALID INPUT>" and return if r<0
	end
	p r
end

#solve("247_intermediate_input1.txt")
#solve("247_intermediate_input2.txt")
solve("247_intermediate_input3.txt")
#solve("247_intermediate_input4.txt")



//
// /r/dailyprogrammer Challenge #245 [Hard] 
//            Guess Who(is)?           
// 										   
// Short Summary: Write a program that takes in a list of IP ranges and detect 
//				  who is viewing your site (via provided list of IPs) then output
//				  a total detailing how many IPs view from which place		   
// 										   
// Full Problem: https://www.reddit.com/r/dailyprogrammer/comments/3xdmtw/20151218_challenge_245_hard_guess_whois/
//  

// Not a fully implemented solution. There's a flaw somewhere in 'isInRange' of my IPRange, but I haven't found the time to fix it.

import scala.io.Source

class IP(val o1: Int, val o2: Int, val o3: Int, val o4: Int) {
	for(i<-List(o1,o2,o3,o4)) if(i > 255||i < 0) throw new Exception
	override def toString: String = s"$o1.$o2.$o3.$o4"
}

class IPRange(val from: IP, val to: IP, val name: String) {
	var ips: List[IP] = List[IP]()
	def isInRange(i: IP): Boolean = {
		if (!(from.o1 to to.o1).contains(i.o1)) false
		else i.o1 match {
			case from.o1 if i.o2 < from.o2 => false 
			case to.o1 if i.o2 > to.o2 => false
			case from.o1 => i.o2 match {
				case from.o2 if i.o3 < from.o3 => false 
				case to.o2 if i.o3 > to.o3 => false
				case _ => i.o3 match {
					case from.o3 if i.o4 < from.o4 => false 
					case to.o3 if i.o4 > to.o4 => false
					case _ => true
				}
			}
			case to.o1 => i.o2 match {
				case from.o2 if i.o3 < from.o3 => false 
				case to.o2 if i.o3 > to.o3 => false
				case from.o2 => i.o3 match {
					case from.o3 if i.o4 < from.o4 => false 
					case to.o3 if i.o4 > to.o4 => false
					case _ => true
				}
				case to.o2 => i.o3 match {
					case from.o3 if i.o4 < from.o4 => false 
					case to.o3 if i.o4 > to.o4 => false
					case _ => true
				}
				case _ => true
			}
			case _ => true
		}
	}
	def addToRange(i: IP): Boolean = 
		if(isInRange(i)) {
			ips = ips :+ i
			true
		} else false
	def count: Int = ips.length
	override def toString: String = s"$name: $from to $to"
}

var ranges: List[IPRange] = List()
var unknown: IPRange = new IPRange(new IP(0,0,0,0), new IP(255,255,255,255), "<unknown>")
for(i<-Source.fromFile("245_hard_input1.txt").getLines()) {
	val v = i.split(' ')
	val (ip1, ip2) = (v(0).split('.').map(_.toInt), v(1).split('.').map(_.toInt))
	ranges = ranges :+ new IPRange(new IP(ip1(0),ip1(1),ip1(2),ip1(3)), new IP(ip2(0),ip2(1),ip2(2),ip2(3)), v.slice(2,v.length).mkString(" "))
}
for(i<-Source.fromFile("245_hard_input2.txt").getLines()) {
	val ip_v = i.split('.').map(_.toInt)
	val ip = new IP(ip_v(0), ip_v(1), ip_v(2), ip_v(3))
	val r = for(q<-ranges) yield q.addToRange(ip)
	if (!r.contains(true)) unknown.addToRange(ip)
}
for(i<-ranges.sortWith(_.count > _.count)) {
	if (i.count!=0) println(s"${i.count} - ${i.name}")
}


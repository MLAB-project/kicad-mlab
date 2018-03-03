e = 0.65;
ps = 0.4;
$fn = 100;

difference(){
translate([-2,-2,0.02]) cube([4,4,0.75]);
translate([1.5,1.5,0.7]) cylinder(0.3,0.3,0.1);
}
translate([e*0.5-ps/2,-2.01, 0]) cube([ps, ps, 0.2]);
translate([e*1.5-ps/2,-2.01, 0]) cube([ps, ps, 0.2]);
translate([e*-0.5-ps/2,-2.01, 0]) cube([ps, ps, 0.2]);
translate([e*-1.5-ps/2,-2.01, 0]) cube([ps, ps, 0.2]);

translate([e*0.5-ps/2, 2.01-ps, 0]) cube([ps, ps, 0.2]);
translate([e*1.5-ps/2, 2.01-ps, 0]) cube([ps, ps, 0.2]);
translate([e*-0.5-ps/2, 2.01-ps, 0]) cube([ps, ps, 0.2]);
translate([e*-1.5-ps/2, 2.01-ps, 0]) cube([ps, ps, 0.2]);

translate([2.01-ps, e*-1.5-ps/2, 0]) cube([ps, ps, 0.2]);
translate([2.01-ps, e*-0.5-ps/2, 0]) cube([ps, ps, 0.2]);
translate([2.01-ps, e*0.5-ps/2, 0]) cube([ps, ps, 0.2]);
translate([2.01-ps, e*1.5-ps/2, 0]) cube([ps, ps, 0.2]);

translate([-2.01, e*-1.5-ps/2, 0]) cube([ps, ps, 0.2]);
translate([-2.01, e*-0.5-ps/2, 0]) cube([ps, ps, 0.2]);
translate([-2.01, e*0.5-ps/2, 0]) cube([ps, ps, 0.2]);
translate([-2.01, e*1.5-ps/2, 0]) cube([ps, ps, 0.2]);
global_settings {
	ambient_light rgb <0.200000002980232, 0.200000002980232, 0.200000002980232>
	max_trace_level 15
}

background { color rgb <1,1,1> }

camera {
	perspective
	location <-0.0161996119080051, -0.234599803051451, -20.3278497017334>
	angle 40
	up <-0.0693826708110603, -0.997546504090806, 0.00932829927347668>
	right <0.997589908759076, -0.0693856897498244, 0> * 0.796675
	direction <0.000647250479282966, 0.00930581722110496, 0.999956490469793> }

light_source {
	<35.7784284430423, -36.4587829093461, -47.463339437814>
	color rgb <1, 1, 1>
	fade_distance 95.5547909902272
	fade_power 0
	parallel
	point_at <-35.7784284430423, 36.4587829093461, 47.463339437814>
}

light_source {
	<-40.4347829604612, -30.487763200236, 24.1996356468076>
	color rgb <0.300000011920929, 0.300000011920929, 0.300000011920929>
	fade_distance 95.5547909902272
	fade_power 0
	parallel
	point_at <40.4347829604612, 30.487763200236, -24.1996356468076>
}

#default {
	finish {ambient .8 diffuse 1 specular 1 roughness .005 metallic 0.5}
}

union {
}
merge {
}
union {
}
union {
cylinder {
	<4.630788, 1.175839, -0.00059>, 	<4.23412035037595, 0.959376311965568, -0.000502439079171431>, 0.1
	pigment { rgbt <0.75, 0.75, 0.75, 0> }
}
cylinder {
	<4.23412035037595, 0.959376311965568, -0.000502439079171431>, 	<3.679448, 0.65669, -0.00038>, 0.1
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464, 0> }
}
cylinder {
	<-4.630788, 1.175839, -0.00059>, 	<-4.23412035051383, 0.959376312040812, -0.000506608646858922>, 0.1
	pigment { rgbt <0.75, 0.75, 0.75, 0> }
}
cylinder {
	<-4.23412035051383, 0.959376312040812, -0.000506608646858922>, 	<-3.679448, 0.65669, -0.00039>, 0.1
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464, 0> }
}
cylinder {
	<-4.587768, -1.312179, -0.00037>, 	<-4.19890942284699, -1.08214728707485, -0.000307458412063657>, 0.1
	pigment { rgbt <0.75, 0.75, 0.75, 0> }
}
cylinder {
	<-4.19890942284699, -1.08214728707485, -0.000307458412063657>, 	<-3.655128, -0.76047, -0.00022>, 0.1
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464, 0> }
}
cylinder {
	<4.587768, -1.312179, -0.00035>, 	<4.19890942294265, -1.08214728713144, -0.000291627851273772>, 0.1
	pigment { rgbt <0.75, 0.75, 0.75, 0> }
}
cylinder {
	<4.19890942294265, -1.08214728713144, -0.000291627851273772>, 	<3.655128, -0.76047, -0.00021>, 0.1
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464, 0> }
}
cylinder {
	<-3.52947008282979, 0.659263783455608, -0.000389903705026662>, 	<-3.51731008282979, -0.0493162165443919, -0.000304903705026662>, 0.1
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464, 0> }
}
cylinder {
	<-3.82942591717021, 0.654116216544392, -0.00039009629497332>, 	<-3.81726591717021, -0.0544637834556081, -0.00030509629497332>, 0.1
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464, 0> }
}
cylinder {
	<-3.51731008282979, -0.0493162165443918, -0.000304903705026662>, 	<-3.50515008282979, -0.757896216544392, -0.000219903705026662>, 0.1
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464, 0> }
}
cylinder {
	<-3.81726591717021, -0.0544637834556082, -0.00030509629497332>, 	<-3.80510591717021, -0.763043783455608, -0.00022009629497332>, 0.1
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464, 0> }
}
cylinder {
	<-3.679448, 0.65669, -0.00039>, 	<-3.0880535, 1.0132845, -0.00033>, 0.1
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464, 0> }
}
cylinder {
	<-3.0880535, 1.0132845, -0.00033>, 	<-2.496659, 1.369879, -0.00027>, 0.1
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464, 0> }
}
cylinder {
	<3.82942591717073, 0.654116216581975, -0.000379782920204657>, 	<3.81726591717073, -0.0544637834180251, -0.000294782920204657>, 0.1
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464, 0> }
}
cylinder {
	<3.52947008282927, 0.659263783418025, -0.000380217079795325>, 	<3.51731008282927, -0.0493162165819749, -0.000295217079795325>, 0.1
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464, 0> }
}
cylinder {
	<3.81726591717073, -0.0544637834180252, -0.000294782920204657>, 	<3.80510591717073, -0.763043783418025, -0.000209782920204657>, 0.1
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464, 0> }
}
cylinder {
	<3.51731008282927, -0.0493162165819748, -0.000295217079795325>, 	<3.50515008282927, -0.757896216581975, -0.000210217079795325>, 0.1
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464, 0> }
}
cylinder {
	<3.679448, 0.65669, -0.00038>, 	<3.0880535, 1.0132845, -0.000325>, 0.1
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464, 0> }
}
cylinder {
	<3.0880535, 1.0132845, -0.000325>, 	<2.496659, 1.369879, -0.00027>, 0.1
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464, 0> }
}
cylinder {
	<2.516609, 2.454879, -0.00037>, 	<2.50828855903522, 2.00236378963478, -0.000328293528998598>, 0.1
	pigment { rgbt <0.75, 0.75, 0.75, 0> }
}
cylinder {
	<2.50828855903522, 2.00236378963478, -0.000328293528998598>, 	<2.496659, 1.369879, -0.00027>, 0.1
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464, 0> }
}
cylinder {
	<-3.655128, -0.76047, -0.00022>, 	<-3.0517235, -1.0973145, -7e-05>, 0.1
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464, 0> }
}
cylinder {
	<-3.0517235, -1.0973145, -7e-05>, 	<-2.448319, -1.434159, 8e-05>, 0.1
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464, 0> }
}
cylinder {
	<3.655128, -0.76047, -0.00021>, 	<3.0517235, -1.0973145, -6e-05>, 0.1
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464, 0> }
}
cylinder {
	<3.0517235, -1.0973145, -6e-05>, 	<2.448319, -1.434159, 9e-05>, 0.1
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464, 0> }
}
cylinder {
	<2.56721501535677, 1.23750887993182, -0.000266820295591396>, 	<1.95254001535677, 0.909874379931817, -6.68202955913963e-05>, 0.1
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464, 0> }
}
cylinder {
	<2.42610298464323, 1.50224912006818, -0.000273179704408585>, 	<1.81142798464323, 1.17461462006818, -7.31797044085853e-05>, 0.1
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464, 0> }
}
cylinder {
	<1.95254001535677, 0.909874379931817, -6.68202955913963e-05>, 	<1.33786501535677, 0.582239879931817, 0.000133179704408604>, 0.1
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464, 0> }
}
cylinder {
	<1.81142798464323, 1.17461462006818, -7.31797044085853e-05>, 	<1.19675298464323, 0.846980120068183, 0.000126820295591415>, 0.1
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464, 0> }
}
cylinder {
	<-2.516609, 2.454879, -0.00036>, 	<-2.50828855903656, 2.00236378970738, -0.000322464176104759>, 0.1
	pigment { rgbt <0.75, 0.75, 0.75, 0> }
}
cylinder {
	<-2.50828855903656, 2.00236378970738, -0.000322464176104759>, 	<-2.496659, 1.369879, -0.00027>, 0.1
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464, 0> }
}
cylinder {
	<-2.42610298467915, 1.50224912009079, -0.000273032279538425>, 	<-1.81142798467915, 1.17461462009079, -7.30322795384247e-05>, 0.1
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464, 0> }
}
cylinder {
	<-2.56721501532085, 1.23750887990921, -0.000266967720461557>, 	<-1.95254001532085, 0.909874379909212, -6.69677204615569e-05>, 0.1
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464, 0> }
}
cylinder {
	<-1.81142798467915, 1.17461462009079, -7.30322795384247e-05>, 	<-1.19675298467915, 0.846980120090788, 0.000126967720461575>, 0.1
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464, 0> }
}
cylinder {
	<-1.95254001532085, 0.909874379909212, -6.69677204615569e-05>, 	<-1.33786501532085, 0.582239879909212, 0.000133032279538443>, 0.1
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464, 0> }
}
cylinder {
	<-2.448319, -1.434159, 8e-05>, 	<-2.43556289875749, -2.06618067435913, 0.000132470251911595>, 0.1
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464, 0> }
}
cylinder {
	<-2.43556289875749, -2.06618067435913, 0.000132470251911595>, 	<-2.426439, -2.518239, 0.00017>, 0.1
	pigment { rgbt <0.75, 0.75, 0.75, 0> }
}
cylinder {
	<-2.52365616073694, -1.30445043358148, 7.687775244564e-05>, 	<-1.91684116073694, -0.952000933581481, 0.00013687775244564>, 0.1
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464, 0> }
}
cylinder {
	<-2.37298183926306, -1.56386756641852, 8.31222475543784e-05>, 	<-1.76616683926306, -1.21141806641852, 0.000143122247554378>, 0.1
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464, 0> }
}
cylinder {
	<-1.91684116073694, -0.952000933581481, 0.00013687775244564>, 	<-1.31002616073694, -0.599551433581481, 0.00019687775244564>, 0.1
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464, 0> }
}
cylinder {
	<-1.76616683926306, -1.21141806641852, 0.000143122247554378>, 	<-1.15935183926306, -0.858968566418519, 0.000203122247554378>, 0.1
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464, 0> }
}
cylinder {
	<2.448319, -1.434159, 9e-05>, 	<2.43556289875749, -2.06618067435913, 0.000142470251911595>, 0.1
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464, 0> }
}
cylinder {
	<2.43556289875749, -2.06618067435913, 0.000142470251911595>, 	<2.426439, -2.518239, 0.00018>, 0.1
	pigment { rgbt <0.75, 0.75, 0.75, 0> }
}
cylinder {
	<2.37298183924981, -1.56386756641452, 9.29648326105666e-05>, 	<1.76616683924981, -1.21141806641452, 0.000152964832610567>, 0.1
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464, 0> }
}
cylinder {
	<2.52365616075019, -1.30445043358548, 8.70351673894518e-05>, 	<1.91684116075019, -0.952000933585479, 0.000147035167389452>, 0.1
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464, 0> }
}
cylinder {
	<1.76616683924981, -1.21141806641452, 0.000152964832610567>, 	<1.15935183924981, -0.858968566414521, 0.000212964832610567>, 0.1
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464, 0> }
}
cylinder {
	<1.91684116075019, -0.952000933585479, 0.000147035167389452>, 	<1.31002616075019, -0.599551433585479, 0.000207035167389452>, 0.1
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464, 0> }
}
cylinder {
	<0, 2.205399, -0.86997>, 	<0, 1.92454119294334, -0.505946636575628>, 0.1
	pigment { rgbt <0.75, 0.75, 0.75, 0> }
}
cylinder {
	<0, 1.92454119294334, -0.505946636575628>, 	<0, 1.533729, 0.00059>, 0.1
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464, 0> }
}
cylinder {
	<1.267309, 0.71461, 0.00013>, 	<1.250999, -0.00732500000000003, 0.00017>, 0.1
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464, 0> }
}
cylinder {
	<1.250999, -0.00732500000000003, 0.00017>, 	<1.234689, -0.72926, 0.00021>, 0.1
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464, 0> }
}
cylinder {
	<1.267309, 0.71461, 0.00013>, 	<0.6336545, 1.1241695, 0.00036>, 0.1
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464, 0> }
}
cylinder {
	<0.6336545, 1.1241695, 0.00036>, 	<0, 1.533729, 0.00059>, 0.1
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464, 0> }
}
cylinder {
	<1.234689, -0.72926, 0.00021>, 	<0.6173445, -1.0743295, 0.00026>, 0.1
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464, 0> }
}
cylinder {
	<0.6173445, -1.0743295, 0.00026>, 	<0, -1.419399, 0.00031>, 0.1
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464, 0> }
}
cylinder {
	<-1.267309, 0.71461, 0.00013>, 	<-1.250999, -0.00732500000000003, 0.000165>, 0.1
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464, 0> }
}
cylinder {
	<-1.250999, -0.00732500000000003, 0.000165>, 	<-1.234689, -0.72926, 0.0002>, 0.1
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464, 0> }
}
cylinder {
	<-1.267309, 0.71461, 0.00013>, 	<-0.6336545, 1.1241695, 0.00036>, 0.1
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464, 0> }
}
cylinder {
	<-0.6336545, 1.1241695, 0.00036>, 	<0, 1.533729, 0.00059>, 0.1
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464, 0> }
}
cylinder {
	<-1.234689, -0.72926, 0.0002>, 	<-0.6173445, -1.0743295, 0.000255>, 0.1
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464, 0> }
}
cylinder {
	<-0.6173445, -1.0743295, 0.000255>, 	<0, -1.419399, 0.00031>, 0.1
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464, 0> }
}
cylinder {
	<0, -1.419399, 0.00031>, 	<0, -2.05165399990435, 0.000339149339328561>, 0.1
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464, 0> }
}
cylinder {
	<0, -2.05165399990435, 0.000339149339328561>, 	<0, -2.503909, 0.00036>, 0.1
	pigment { rgbt <0.75, 0.75, 0.75, 0> }
}
cylinder {
	<0, 1.533729, 0.00059>, 	<0, 1.92399994201129, 0.507545402027005>, 0.1
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464, 0> }
}
cylinder {
	<0, 1.92399994201129, 0.507545402027005>, 	<0, 2.204469, 0.87187>, 0.1
	pigment { rgbt <0.75, 0.75, 0.75, 0> }
}
sphere {
	<3.655128, -0.76047, -0.00021>, 0.51
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464,0> }
}
sphere {
	<2.448319, -1.434159, 9e-05>, 0.51
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464,0> }
}
sphere {
	<1.234689, -0.72926, 0.00021>, 0.51
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464,0> }
}
sphere {
	<1.267309, 0.71461, 0.00013>, 0.51
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464,0> }
}
sphere {
	<2.496659, 1.369879, -0.00027>, 0.51
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464,0> }
}
sphere {
	<3.679448, 0.65669, -0.00038>, 0.51
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464,0> }
}
sphere {
	<0, -1.419399, 0.00031>, 0.51
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464,0> }
}
sphere {
	<0, 1.533729, 0.00059>, 0.51
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464,0> }
}
sphere {
	<-1.267309, 0.71461, 0.00013>, 0.51
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464,0> }
}
sphere {
	<-1.234689, -0.72926, 0.0002>, 0.51
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464,0> }
}
sphere {
	<-2.448319, -1.434159, 8e-05>, 0.51
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464,0> }
}
sphere {
	<-2.426439, -2.518239, 0.00017>, 0.33
	pigment { rgbt <0.75, 0.75, 0.75,0> }
}
sphere {
	<-3.655128, -0.76047, -0.00022>, 0.51
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464,0> }
}
sphere {
	<-3.679448, 0.65669, -0.00039>, 0.51
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464,0> }
}
sphere {
	<-2.496659, 1.369879, -0.00027>, 0.51
	pigment { rgbt <0.400000005960464, 0.400000005960464, 0.400000005960464,0> }
}
sphere {
	<0, -2.503909, 0.00036>, 0.33
	pigment { rgbt <0.75, 0.75, 0.75,0> }
}
sphere {
	<4.587768, -1.312179, -0.00035>, 0.33
	pigment { rgbt <0.75, 0.75, 0.75,0> }
}
sphere {
	<2.426439, -2.518239, 0.00018>, 0.33
	pigment { rgbt <0.75, 0.75, 0.75,0> }
}
sphere {
	<2.516609, 2.454879, -0.00037>, 0.33
	pigment { rgbt <0.75, 0.75, 0.75,0> }
}
sphere {
	<4.630788, 1.175839, -0.00059>, 0.33
	pigment { rgbt <0.75, 0.75, 0.75,0> }
}
sphere {
	<0, 2.204469, 0.87187>, 0.33
	pigment { rgbt <0.75, 0.75, 0.75,0> }
}
sphere {
	<-4.587768, -1.312179, -0.00037>, 0.33
	pigment { rgbt <0.75, 0.75, 0.75,0> }
}
sphere {
	<-4.630788, 1.175839, -0.00059>, 0.33
	pigment { rgbt <0.75, 0.75, 0.75,0> }
}
sphere {
	<-2.516609, 2.454879, -0.00036>, 0.33
	pigment { rgbt <0.75, 0.75, 0.75,0> }
}
sphere {
	<0, 2.205399, -0.86997>, 0.33
	pigment { rgbt <0.75, 0.75, 0.75,0> }
}
}
merge {
}
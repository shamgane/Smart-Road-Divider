# Smart-Road-Divider

Metropolitan and cosmopolitan cities, being the IT hubs and job centers, tend to attract swarms of crowd into them. With increasing population in
these cities, there is an exponential rise in the number of vehicles, especially during the morning and evening hours of travelling to and
from the workplaces. This often results in a complete blocking on one
side of the road- the one leading to the workplace building in the
morning hours and the opposite side of the road during the evening
hours- whereas the other side of the road has very less traffic.This pattern
motivates us to come up with an idea of movable dividers which can
expand the road width of that side of the road where the traffic is more
and reduce the width on the other side where the traffic is sparse. 

The idea is to deploy cameras facing either sides of the roads with major
traffic blocks. The camera images will be constantly analyzed to check
for the percentage of road visible and also the speed of the vehicles
moving. If it is below a threshold value for more than a set duration of
time (example : the traffic block has been persistent for more than 15
minutes on one side of the road and the other side is having a free
movement of vehicles), at the time of the next cycle of red light on the
traffic signal, the dividers will be shifted towards the side of less traffic, creating more space for the other side vehicles.

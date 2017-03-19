This was with `max_iterations=200, restart_after=100`.

I noticed a lot of slowdown from keeping around large matrices. As I got close
to the restart it was very noticeable. This is clear from the profile. It spent
a lot of time in QR solving. Recommend restart <50. Maybe around 30 was where
it was quite quick. It would be interesting to profile if/how much these larger
matrices move us closer to target compared to the smaller ones. I could come up
with a error_delta / time weight.

I ended up with error of: `14358819.9043`.

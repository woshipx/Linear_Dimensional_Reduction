function d = SphereDist2(x,y,R)

if nargin < 3
    R = 6378.137;
end
x = deg2rad(x);
y = deg2rad(y);
h = HaverSin(abs(x(2)-y(2)))+cos(x(2))*cos(y(2))*HaverSin(abs(x(1)-y(1)));
d = 2 * R * asin(sqrt(h));

function h = HaverSin(theta)
    h=sin(theta/2)^2;
end

end


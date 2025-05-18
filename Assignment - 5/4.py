import numpy as np;
import matplotlib.pyplot as pl;
x = np.linspace(-10,10,100);
y1 = x**2;
y2 = np.sin(x);
y3 = np.exp(x);
y4 = np.log(np.abs(x) + 1);

pl.plot(x,y1);
pl.title("Y = X^2");
pl.xlabel("X");
pl.ylabel("Y");
pl.grid(True);
pl.show();

pl.plot(x,y2);
pl.title("Y = sin(X)");
pl.xlabel("X");
pl.ylabel("Y");
pl.grid(True);
pl.show();

pl.plot(x,y3);
pl.title("Y = e^X");
pl.xlabel("X");
pl.ylabel("Y");
pl.grid(True);
pl.show();

pl.plot(x,y4);
pl.title("Y = log(|x| + 1)");
pl.xlabel("X");
pl.ylabel("Y");
pl.grid(True);
pl.show();
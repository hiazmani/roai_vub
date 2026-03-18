library(deSolve)

rashevsky<- function( t,y, parms )
{
	dy<-y
	dy[1]<-(1-exp(-parms$a*pmax(0,y[2]-parms$h2))) - y[1]/parms$alpha
#	dy[2]<-(1-(1-exp(-parms$a*pmax(0,y[1]-parms$h1)))) - y[2]/parms$alpha
	dy[2]<-((1-exp(-parms$a*pmax(0,y[1]-parms$h1)))) - y[2]/parms$alpha
	return( list(unlist(dy)) )
}

times<-seq(0,10,0.01)
y<-c( 1,1)
parms<-{}
parms$h1<-0.3
parms$h2<-0.3
parms$a<-4
parms$alpha<-1


x<-seq(0,4,0.01)

#plot( x, 1-(1-exp(-parms$a*pmax( 0,x-parms$h2 ))), type='l',xlim=c(0,1.5),ylim=c(0,1.5),lwd=2, xlab='e2',ylab='e1')
plot( x, (1-exp(-parms$a*pmax( 0,x-parms$h2 ))), type='l',xlim=c(0,1.5),ylim=c(0,1.5),lwd=2, xlab='e2',ylab='e1')
lines((1-exp(-parms$a*pmax( 0,x-parms$h1 ))), x, lty=2, lwd=2)

c0<-seq( 0,1.5,0.25)
for( index in seq( 1,length(c0)))
{
	y[1]<-c0[index]
	y[2]<-0
	sol<-ode( y, times, rashevsky, parms )
	lines( sol[,2], sol[,3],type='l')
}

for( index in seq( 1,length(c0)))
{
	y[1]<-c0[index]
	y[2]<-1.5
	sol<-ode( y, times, rashevsky, parms )
	lines( sol[,2], sol[,3],type='l')
}

for( index in seq( 1,length(c0)))
{
	y[2]<-c0[index]
	y[1]<-0
	sol<-ode( y, times, rashevsky, parms )
	lines( sol[,2], sol[,3],type='l')
}

for( index in seq( 1,length(c0)))
{
	y[2]<-c0[index]
	y[1]<-1.5
	sol<-ode( y, times, rashevsky, parms )
	lines( sol[,2], sol[,3],type='l')
}

y[1] <- 0
y[2] <- 0.9779547
sol<-ode( y, times, rashevsky, parms )
lines( sol[,2], sol[,3],type='l', lty=4)
#lines( sol[,3], sol[,2],type='l', lty=4)

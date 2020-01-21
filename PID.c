//PID Code
float kp=1.3;
float ki=0.1;
float kp=0.2;
float current=0;
float activezone;
float setpoint=0;
float angle;
float error;
float errort;
float lasterror;
float p;
float i;
float d;
void setup() {
  // put your setup code here, to run once:

}

void loop() {
  // put your main code here, to run repeatedly:
  	error=setpoint-angle;
	if(error<activezone && error!=0)
	{
  		errort+=error;
	}
	else{ error=0; }
	if(errort>50/ki)
	{ 
		errort=50/ki;
	}

	if(error==0)
	{ 
		d=0;
	}

	p=error*kp;
	i=errort*ki;
	d=(error-lasterror)*kd;
	lasterror=error;


	current=p+i+d;

	if(angle=0)
	{ 
		current=0; 
	}
	if(current<0)
	{ 
		current=0;
	}


}
#include <Adafruit_MPU6050.h>

Adafruit_MPU6050 mpu;

void setup() 
{ 
  // Flex Sensor
  Serial.begin(115200);
  pinMode(PA0, INPUT);
  pinMode(PA1, INPUT);
  pinMode(PA2, INPUT);
  pinMode(PA3, INPUT);
  pinMode(PA4, INPUT);
  
  
  // MPU6050
  // Try to initialize!
	if (!mpu.begin()) {
		Serial.println("Failed to find MPU6050 chip");
		while (1) {
		  delay(10);
		}
	}
	Serial.println("MPU6050 Found!");

	// set accelerometer range to +-8G
	mpu.setAccelerometerRange(MPU6050_RANGE_8_G);

	// set gyro range to +- 500 deg/s
	mpu.setGyroRange(MPU6050_RANGE_500_DEG);

	// set filter bandwidth to 21 Hz
	mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);

	delay(100);

} 
 
void loop() 
{ 
  //MPU6050
  /* Get new sensor events with the readings */
	sensors_event_t a, g, temp;
	mpu.getEvent(&a, &g, &temp);

	/* Print out the values */
	//Serial.print("Acceleration X: ");
	Serial.print(float(a.acceleration.x));
	Serial.print(" ");
	Serial.print(float(a.acceleration.y));
	Serial.print(" ");
	Serial.print(float(a.acceleration.z));
	Serial.print(" ");

	//Serial.print("Rotation X: ");
	Serial.print(float(g.gyro.x));
	Serial.print(" ");
	Serial.print(float(g.gyro.y));
	Serial.print(" ");
	Serial.print(float(g.gyro.z));
	Serial.print(" ");

  // Flex Sensor
  Serial.print(float(analogRead(PA4)));
  Serial.print(" ");
  Serial.print(float(analogRead(PA3)));
  Serial.print(" ");
  Serial.print(float(analogRead(PA2)));
  Serial.print(" ");
  Serial.print(float(analogRead(PA1)));
  Serial.print(" ");
  Serial.print(float(analogRead(PA0)));
  Serial.println("\n");
  
  delay(20);
}
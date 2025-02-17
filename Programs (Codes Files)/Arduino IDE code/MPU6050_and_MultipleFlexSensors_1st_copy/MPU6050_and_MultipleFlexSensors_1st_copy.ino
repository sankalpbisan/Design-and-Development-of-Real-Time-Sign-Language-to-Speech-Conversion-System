#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <Wire.h>

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
  // Flex Sensor
  int f1 = analogRead(PA0);    // read the ADC value from pin A7
  int f2 = analogRead(PA1);    // read the ADC value from pin A7
  int f3 = analogRead(PA2);    // read the ADC value from pin A7
  int f4 = analogRead(PA3);    // read the ADC value from pin A7
  int f5 = analogRead(PA4);    // read the ADC value from pin A7

  Serial.println(f1);
  Serial.println(f2);
  Serial.println(f3);
  Serial.println(f4);
  Serial.println(f5);
  Serial.println("-----------------------");
  Serial.println("");
 // delay(500);

  //MPU6050
  /* Get new sensor events with the readings */
	sensors_event_t a, g, temp;
	mpu.getEvent(&a, &g, &temp);

	/* Print out the values */
	Serial.print("Acceleration X: ");
	Serial.print(a.acceleration.x);
	Serial.print(", Y: ");
	Serial.print(a.acceleration.y);
	Serial.print(", Z: ");
	Serial.print(a.acceleration.z);
	Serial.println(" m/s^2");

	Serial.print("Rotation X: ");
	Serial.print(g.gyro.x);
	Serial.print(", Y: ");
	Serial.print(g.gyro.y);
	Serial.print(", Z: ");
	Serial.print(g.gyro.z);
	Serial.println(" rad/s");

	Serial.print("Temperature: ");
	Serial.print(temp.temperature);
	Serial.println(" degC");

	Serial.println("");
	delay(500);
}
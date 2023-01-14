long duration, cm;
void setup() {
  Serial.begin(9600);
  pinMode(12, OUTPUT);    /*Trig為發送訊號*/
  pinMode(13, INPUT);     /*Echo為接收訊號*/
  pinMode(6,OUTPUT);      /*蜂鳴器*/
  pinMode(7,OUTPUT);      /*馬達*/
  pinMode(11,OUTPUT);     /*綠燈*/
  pinMode(10,OUTPUT);     /*黃燈*/
  pinMode(9,OUTPUT);      /*紅燈*/
}
void loop() {
  /*用紅外線測距離水面多遠*/
  digitalWrite(12, HIGH);
  delayMicroseconds(1000);
  digitalWrite(12, LOW);
  duration=pulseIn(13, HIGH);
  cm=microsecondsToCentimeters(duration);
  Serial.print(cm);
  Serial.print(" cm");
  Serial.println();
  if(cm>23.5){
    digitalWrite(11, HIGH);  /*綠燈亮*/
    digitalWrite(9, LOW);    /*紅燈暗*/
    digitalWrite(10, LOW);   /*黃燈暗*/    
    digitalWrite(7, LOW);    /*抽水馬達關閉*/
    digitalWrite(6, LOW);    /*水高小於5cm時蜂鳴器關閉*/
  }
  else if(cm>22 and cm<=23){
    digitalWrite(11, LOW);  /*綠燈暗*/
    digitalWrite(9, LOW);   /*紅燈暗*/
    digitalWrite(10, HIGH); /*黃燈亮*/    
    digitalWrite(7, HIGH);   /*抽水馬達關閉*/
    digitalWrite(6, LOW);   /*水高小於5cm時蜂鳴器關閉*/
  }
  else if(cm<=22 and cm>20){
    digitalWrite(11, LOW); /*綠燈暗*/
    digitalWrite(10, LOW); /*黃燈暗*/
    digitalWrite(9, HIGH); /*紅燈亮*/
    digitalWrite(6, LOW);  /*水高小於5cm時蜂鳴器關閉*/
    digitalWrite(7, HIGH); /*抽水馬達啟動*/
  }
   else if(cm<=20){
    digitalWrite(11, LOW); /*綠燈暗*/
    digitalWrite(10, LOW); /*黃燈暗*/
    digitalWrite(9, HIGH); /*紅燈亮*/
    digitalWrite(6, HIGH); /*水高大於5cm時蜂鳴器響*/
    digitalWrite(7, HIGH); /*抽水馬達啟動*/
  }
  delay(1000);
}
long microsecondsToCentimeters(long microseconds){
  return microseconds / 29 / 2; //Convert 340m/s to cm/microSecond
}

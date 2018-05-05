

void setup()
{
    //Define os pinos dos leds como saida
  pinMode(3, OUTPUT);
  
  Serial.begin(9600);
  Serial.println("Serial ready");

  setup2();
}

void loop()
{
  char buf;
  String comando;

  while(Serial.available() > 0)
  {
    delay(10);
    buf = Serial.read();
    //Caso seja recebido R, acende o led vermelho
    if (buf == '#') 
        {
          Serial.println("RECEBEU");
          break;                     //Exit the loop when the # is detected after the word
     
    }  
    comando += buf; 
     

  }
  
  if (comando == "amarelo")
    {
      digitalWrite(3, HIGH);
      Serial.println("LED Vermelho ligado !");
    }
    //Caso seja recebido G, acende o led verde
    if (comando == "vermelho")
    {
      digitalWrite(3, LOW);
      Serial.println("LED Verde ligado !");
    }

    comando ="";

  
}

## PROJECT
# Code a Mars Landing

Na NASA, o processo que chamamos de entrada, descida e pouso, ou EDL, é a série de eventos que ocorre desde o momento em que uma espaçonave encontra o topo da atmosfera marciana até pousar com segurança na superfície. Você pode modelar esse processo usando linguagens de codificação, como Python! Nesta atividade, você programará vários recursos do EDL, como determinar a proximidade da sua espaçonave em relação à superfície quando ela chegar a Marte.

![codingedl_step4](https://github.com/IMNascimento/Code_a_Mars_Landing/assets/28989407/571ef69b-466b-45e2-9da7-475331f40ad3)


## Materials

- [ ] Dispositivo capaz de executar código Python
- [ ] Software de edição Python gratuito, como VsCode ou Atom
- [ ] Sensor de luz
- [ ] LEDs de várias cores
- [ ] Botões programáveis
- [ ] Sensor ultrasônico
- [ ] Buzzer or speaker
- [ ] Cabos conectores e  breadboard
- [ ] Embora esta atividade possa ser concluída usando componentes individuais, existem vários kits com todos esses materiais incluídos, como Cubit, LEGO, Raspberry Pi e Arduino.


![codingedl_step1-640x350](https://github.com/IMNascimento/Code_a_Mars_Landing/assets/28989407/90587972-a973-490d-a403-dc4e00192cf4)

## 1. Aprenda o que é preciso para pousar em Marte

Aterrar uma nave espacial em Marte não é uma tarefa fácil. Devido à enorme distância entre a Terra e Marte, não podemos controlar a espaçonave em tempo real como faríamos em um videogame. Todas as nossas comunicações com a nave espacial são limitadas pela velocidade da luz, por isso leva cerca de sete minutos para um sinal ser enviado da Terra a Marte e mais sete minutos para voltar. Como resultado, as naves espaciais têm de aterrar de forma autónoma – por conta própria, com base em instruções programadas nos seus computadores de bordo.

Para pousar com sucesso uma espaçonave, nós a enviamos ao espaço com centenas de milhares de linhas de código, fornecendo instruções para cada uma das manobras que ela precisará realizar para pousar com segurança, incluindo:

- Medindo a que distância está da superfície
- Saber quando realizar cada manobra, como abrir o pára-quedas
- Comunicando seu status aos controladores de missão na Terra
- E iniciar as operações com segurança ao chegar à superfície

Sobre a imagem: Esta ilustração mostra os eventos que ocorrem nos minutos finais da viagem de quase sete meses que o rover Perseverance da NASA faz a Marte. Crédito da imagem: NASA/JPL-Caltech | › ![Imagem completa e legenda](https://mars.nasa.gov/resources/25489/perseverance-rovers-entry-descent-and-landing-profile/)


## 2. Prepare-se
Revise cada uma das tarefas que você precisará concluir nas etapas abaixo para pousar sua espaçonave com segurança. E obtenha mais inspiração pesquisando ![como a NASA pousa espaçonaves em Marte](https://www.jpl.nasa.gov/edu/learn/video/mars-in-a-minute-how-do-you-land-on-mars/). Em seguida, decida quais dispositivos você usará para simular sua espaçonave e seu pouso. Quais ferramentas você possui para indicar etapas bem-sucedidas ao longo do processo de pouso? Você usaria luzes em determinadas etapas? As luzes devem estar acesas ou apagadas? Você poderia usar som? Alguns dispositivos são capazes de detectar cores – talvez a cor do local de pouso em Marte? Seja tão criativo quanto quiser e personalize-o com base em suas próprias ideias, no que você tem disponível e no que você se sente confortável.

Observação: ao longo desta atividade, forneceremos alguns exemplos de códigos e nomes, mas os seus provavelmente variarão dependendo do que você estiver usando. Apenas lembre-se de ser consistente o tempo todo!

### Tarefas

1. <b>Importe seus componentes</b> – Alguns dispositivos fazem isso automaticamente, enquanto outros usam uma linha de ‘importação’ para acessar sua biblioteca. Cada dispositivo tem suas próprias convenções de nomenclatura e vocabulário.

```python
from components import UltrasonicSensor, LED
from time import sleep

#If your kit doesn't automtically detect the port being used, you can specify
ultrasonic = UltrasonicSensor("D1")

```

## 3. Meça a distância entre a espaçonave e a superfície

Como o nome sugere, a entrada, a descida e o pouso são um processo de várias etapas. Por exemplo, os engenheiros programam o rover para fornecer feedback constante sobre a sua altimetria – altura – à medida que desce em Marte. Depois que uma espaçonave determina que está em uma determinada altitude, ela sabe que deve iniciar a próxima fase da sequência de pouso.

### Tarefas

1. <b>Determine seu local de pouso</b> – Você determinará seu “objetivo de pouso” com base nos dispositivos que está usando para simular o pouso. Por exemplo, se você tiver um pequeno dispositivo para usar como nave espacial, poderá amarrá-lo a um barbante e baixá-lo da borda de uma mesa em direção ao chão. Se o seu dispositivo for maior ou delicado, você pode tentar deslizar o dispositivo horizontalmente pelo chão em direção a uma parede ou a um alvo em pé.

2. <b>Configure um sensor ultrassônico</b> – Comece escrevendo o código para ativar seu sensor ultrassônico e faça com que ele exiba a distância que está lendo.

```python

while True:
    distance = ultrasonic.distance
    print(distance)
    sleep(0.1)

```

3. <b>Adicione um indicador luminoso para refletir a medição</b> – Usando LEDs, podemos criar rapidamente uma saída visual para refletir a medição do sensor ultrassônico. Isso pode ser feito usando um padrão go-caution-stop, mas fique à vontade para torná-lo seu!

```python
red_led = LED("D2")
yellow_led = LED("D3")
green_led = LED("D4")

if distance < 10:
    red_led.on()
    yellow_led.on()
    green_led.on()
elif distance < 20:
    red_led.off()
    yellow_led.on()
    green_led.on()
else:
    red_led.off()
    yellow_led.off()
    green_led.on()

```

![codingedl_step4](https://github.com/IMNascimento/Code_a_Mars_Landing/assets/28989407/571ef69b-466b-45e2-9da7-475331f40ad3)

## 4. Crie um alarme para cada fase do pouso

O rover Perseverance possui uma câmera abaixo dele que pode medir a distância entre ele e a superfície marciana. Isso permite que a espaçonave determine quando realizar cada uma de suas manobras de pouso, como disparar retrofoguetes para desacelerar ainda mais a descida da espaçonave.

### Tarefas

1. <b>Transição entre estágios</b> – Adicione um sistema de alarme que sinaliza quando é hora de passar para a próxima fase do pouso da sua espaçonave, como a implantação dos cabos do skycrane que abaixam o rover até o solo. Um exemplo de alerta de áudio é fornecido abaixo.

```python
from components import Buzzer
buzzer = Buzzer("D5")
if distance < 10:
    red_led.on()
    yellow_led.on()
    green_led.on()
    buzzer.on()
elif distance < 20:
    red_led.off()
    yellow_led.on()
    green_led.on()
else:
    red_led.off()
    yellow_led.off()
    green_led.on()
```

2. <b>Considere como ajustar a altura desejada</b> – O código de exemplo fornecido acima soa o alarme quando nosso código atinge uma determinada leitura de luz e distância. Você pode modificar o código para produzir uma luz verde para implantar na distância desejada – nem muito perto nem muito longe?


![kwl_mars-640x350](https://github.com/IMNascimento/Code_a_Mars_Landing/assets/28989407/5b78a1b5-11fe-4ef1-8b26-89a3d7e717d0)

## 5. Ligue
Enquanto os rovers Perseverance e Curiosity são movidos ![pelo que é conhecido como RTG](https://spaceplace.nasa.gov/what-powers-a-spacecraft/en/), outras missões a Marte utilizam energia solar, coletando luz através de painéis solares e convertendo-a em eletricidade. Assim que essas missões pousarem com segurança, elas começarão a coletar luz para energizá-las e começar a se comunicar com os cientistas na Terra.


### Tarefas

1. <b>Colete luz solar para alimentar sua espaçonave</b> – Usando um sensor de luz ou painel solar, podemos medir quanta luz solar estamos coletando para fornecer energia à nossa espaçonave.

```python
from components import LightSensor
from time import sleep, time

light = LightSensor("D6")
while True:
    lightlevel = (light.reading)
    print lightlevel
```

2. <b>Trace seus dados de energia solar</b> – Dependendo do seu dispositivo ou kit, pode ser possível imprimir uma leitura constante da quantidade de luz que sua espaçonave está coletando ou até mesmo traçar os dados ao longo do tempo. A capacidade de ver isso em tempo real varia dependendo se o monitor está no kit ou no computador.

```python
plt.ion()
fig = plt.figure()
x_data = []
y_data = []
start_time = time()

x_data.append(elapsed_time)
y_data.append(lightlevel)

plt.title("Light Sensor input over time")
plt.ylabel("Light Level")
plt.xlabel("Time in seconds")

plt.plot(x_data, y_data)
plt.draw()
plt.pause(0.01)
```


![miam_phoning-640x350](https://github.com/IMNascimento/Code_a_Mars_Landing/assets/28989407/cc67239f-54a9-4541-8864-0f2f5854861d)

## 6. Telefone para casa
Lembre-se de que, devido à grande distância entre a Terra e Marte, não sabemos realmente se a missão aterrou com sucesso até que nos transmita o seu estado.

### Tarefas

1. <b>Envie uma mensagem usando som</b> – Programe uma campainha para enviar manualmente uma mensagem de volta à Terra, sinalizando que sua espaçonave está segura e ligada. Tente fazer com que a campainha emita uma mensagem simples em código Morse. Um exemplo de dicionário de código Morse pode ser encontrado no trecho de código abaixo.

```python
from components import Button
button = Button("D7")

while True:
    if button.is_pressed:
        buzzer.on()
    else:
        buzzer.off()
```

2. <b>Desafio: Envie a sua mensagem em código em vez de som</b> – As ondas sonoras não podem viajar através do vazio do espaço, por isso não podemos usar o som para que a nave espacial transmita o seu estado seguro de volta à Terra. Em vez disso, podemos fazer com que a espaçonave escreva sua mensagem em código Morse e depois nos transmita essa mensagem usando luz.

```python
Morse_Dict = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.',
'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-',
'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-',
'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--',
'X':'-..-', 'Y':'-.--', 'Z':'--..'}

def encrypt(message):
    convert = ' '
    for letter in message:
        if letter != ' ':
            convert += Morse_Dict[letter] + ' '
        else:
            convert += ' '
    return convert

def decrypt(message):
    message += ' '
    decode = ''
    text = ''
    for letter in message:
        if (letter != ' '):
            i = 0
            text += letter
        else:
            i += 1
            if i == 2:
                decode += ' '
            else:
                decode += list(Morse_Dict.keys())[list(Morse_Dict.values()).index(text)]
                text = ''
    return decode

def main():
    text = input("Enter Message: ")
    output = encrypt(text.upper())
    print(output)
if __name__ == '__main__':
    main()
```


Isto é semelhante à forma como nos comunicamos com as naves espaciais através da ![Deep Space Network da NASA](https://www.nasa.gov/directorates/heo/scan/index.html), ou DSN. Os dados são convertidos em código binário (uns e zeros) por computadores e transmitidos como ondas de luz da espaçonave para as gigantescas antenas parabólicas que compõem o DSN.


![codingedl_step7-640x350](https://github.com/IMNascimento/Code_a_Mars_Landing/assets/28989407/332997e7-3a33-475f-8a2e-0b0cc3e373a8)

## 7. Junte tudo
Como aprendemos, devido à distância entre a Terra e Marte, o nosso código tem de funcionar de forma autónoma. Assim que o EDL começar, nosso código deverá ser executado sozinho do início ao fim.

### Tarefas

<b>Coloque seu código em uma sequência</b> – Como desafio final, veja se você consegue editar seu código para fazer tudo a seguir em sequência:

1. Meça a distância da superfície, passando de um LED vermelho (muito alto para implantar) para um LED amarelo e para um LED verde (altura desejada para implantar).
2. Assim que sua espaçonave atingir a altura desejada da superfície (luz verde), faça com que ela emita um som.
3. Ao reproduzir o som indicando que pousou com segurança, comece a coletar luz.
4. Após 30 segundos de coleta de luz, solicite uma mensagem em código Morse para transmitir de volta à Terra.
5. Assim que a saída do código Morse for recebida (manualmente ou pré-programada), faça com que seu programa saia das operações (desligue os LEDs e pare de coletar luz).



![Projeto Entrada, Descida e Pouso em Marte](https://mars.nasa.gov/insight/entry-descent-landing/)
![Projeto InSight](https://mars.nasa.gov/insight/timeline/landing/entry-descent-landing/)
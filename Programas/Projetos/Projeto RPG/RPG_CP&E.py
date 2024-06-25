# Importação de bibliotecas necessárias
import sys

# Dicionários para armazenar informações sobre classes e tipos
classe_info = {
    1: "Feiticeiro(a)",
    2: "Caçador(a)",
    3: "Bruxo(a) do Caos",
    4: "Criatura"
}

elementos = {
    1: "Ar",
    2: "Água",
    3: "Fogo",
    4: "Gelo",
    5: "Raio",
    6: "Terra"
}

armas = {
    11: "Uma Dupla de Pistolas",
    12: "Arco e Flecha Enfeitiçados",
    13: "Espada Mística",
    14: "Foice do Purgatório",
    15: "Correntes da Justiça"
}

caos = {
    21: "Sombras",
    22: "Insetos",
    23: "Sangue",
    24: "Ossos"
}

criaturas = {
    31: "Dragão",
    32: "Vampiro",
    33: "Lobisomem",
    34: "Minotauro",
    35: "Sereia",
    36: "Harpia",
    37: "Grifo Imperador das Trevas"
}

#Função para dar boas vindas
def bem_vindo():
    print('''======= Seja bem-vindo ao RPG Chronos Primordiais & Elementais! ======= \n
    Nele você poderá escolher sua classe no nosso mundo mágico, suas especialidades e sua arma.
    E não menos importante, enfrentar a máquina, que também fará suas escolhas, para ver qual ser mágico é mais poderoso.\n
    Está pronto? Então que comecem os duelos!''')

#Função padrão para todos os tipos de escolhas
def obter_escolha(mensagem, opcoes):
    while True:
        escolha = input(mensagem).strip()
        if escolha.isdigit() and int(escolha) in opcoes:
            return int(escolha)
        else:
            print("Escolha inválida. Por favor, selecione uma opção válida.")

#Funções de descrição
def ler_descricao_classe(classe):
    info = input("Você quer ler a descrição da classe escolhida? [Respostas: S / N] ").strip().upper()
    return info == 'S'

def ler_descricao_tipo(tipo):
    info = input("Você quer ler a descrição da opção escolhida? [Respostas: S / N] ").strip().upper()
    return info == 'S'

def obter_descricao_classe(classe):
    if classe == 1:
        return '''Os Feiticeiros, seres de porte humano dotados de uma magia interna excepcionalmente poderosa, 
transcendem a essência dos seres comuns. Envolvidos pela aura da Magia Astral, sua conexão com os fluxos mágicos é inigualável, ampliando seus horizontes para além do conhecimento convencional.

Capazes de entrelaçar os mais complexos feitiços e encantamentos, os Feiticeiros desbravam um vasto reino de possibilidades mágicas. 
Eles manipulam a própria essência da vida, moldando-a conforme sua vontade e determinação.

Entre os Feiticeiros, os chamados Feiticeiros Elementais emergem como protagonistas, mergulhando nos elementos primordiais que compõem o universo. 
Desde a leveza do Ar até a densidade da Terra, passando pela volatilidade do Fogo e a fluidez da Água, a intensidade dos Raios e a pureza do Gelo, cada elemento se torna uma extensão de sua vontade.

No entanto, assim como os elementos da natureza, os Feiticeiros Elementais enfrentam desafios e dilemas únicos. As vantagens e fraquezas de cada elemento refletem-se no próprio Feiticeiro, exigindo sabedoria e maestria para equilibrar seus poderes.
'''
    elif classe == 2:
        return '''Os Caçadores, seres mágicos de porte humano dotados de uma magia ligeiramente superior, emergem como guardiões entre os povos humanos desde a antiguidade. 
Apesar de sua magia não alcançar as alturas estonteantes dos Feiticeiros, sua proficiência e conhecimento mágico ultrapassam em muito o dos humanos comuns.

Forjados na encruzilhada entre a magia e a habilidade física, os Caçadores são mestres nas artes marciais e nas técnicas de combate e caça. 
Seus corpos são templos de disciplina e vigor, moldados ao longo de anos de treinamento árduo.

Armaduras encantadas e runas entrelaçadas em suas vestimentas conferem aos Caçadores uma vantagem sobrenatural, equiparando-os aos próprios Feiticeiros em termos de poder e resistência. 
Entretanto, é em seu propósito maior que os Caçadores encontram sua verdadeira vocação: a caça às Criaturas Místicas Malignas.

Nas sombras e nos recantos mais sombrios dos reinos mágicos, os Caçadores marcham, determinados a erradicar a ameaça das criaturas que assombram a existência da humanidade. 
Suas habilidades únicas e sua determinação implacável fazem deles os guardiões incansáveis da paz e da segurança.
'''
    elif classe == 3:
        return '''Os Bruxos do Caos, seres mágicos de porte humano imbuídos de uma magia sinistra e anormal, emergem como arautos do desequilíbrio nos mundos mágicos e não-mágicos. 
Manipuladores das trevas e das sombras, os Bruxos do Caos lançam-se nas profundezas do desconhecido, desafiando os limites da própria existência.

Envolvidos na nebulosidade do Caos, uma magia demoníaca que contraria os princípios da Magia Astral dos Feiticeiros, 
os Bruxos do Caos são dotados de uma inteligência aguçada e astúcia incomparável. Detentores de segredos obscuros e conhecimentos proibidos, são os artífices por trás da criação das armas e amuletos que alimentam o poder dos Feiticeiros e Caçadores.

A magia do Caos que fluí pelos veios de suas almas é uma força primordial, mais mortal e devastadora do que qualquer feitiçaria conhecida. 
Com uma facilidade inata para manipular as energias caóticas, os Bruxos do Caos erguem-se como titãs entre seus rivais, deixando um rastro de destruição e desespero em seu caminho.

No entanto, ao longo dos séculos, os Bruxos e Bruxas do Caos foram caçados e perseguidos implacavelmente, temidos pela sua imensa influência sobre os destinos dos clãs. 
Sua existência permanece envolta em mistério e intriga, uma sombra que se move nos recantos mais sombrios da imaginação.'''
    elif classe == 4:
        return '''As Criaturas, seres mágicos de formas diversas e porte variável, são manifestações da fantasia e da mitologia dos povos de todo canto do mundo. 
Cada uma delas é uma encarnação única da magia, refletindo a diversidade e a exuberância do mundo ao seu redor.

Embora não se valham de feitiços como os Feiticeiros ou Caçadores, algumas Criaturas são dotadas da habilidade de manipular a mana, alterando seus atributos físicos de maneiras surpreendentes e imprevisíveis. 
Essa capacidade metamórfica as torna ainda mais formidáveis diante de seus adversários.

Entre as Criaturas, as mais temíveis são aquelas que remontam às origens primordiais do mundo. 
Descendentes diretas das criaturas ancestrais, como o Dragão, o Vampiro, o Lobisomem, a Sereia, a Harpia e o Minotauro, 
emergem como titãs entre seus pares, cada uma com sua especialidade e nível de ameaça únicos.

Apesar de suas formas e habilidades singulares, todas as Criaturas compartilham uma característica fundamental: uma inteligência equiparável à humana. 
Dotadas de raciocínio e astúcia, esses seres ancestrais navegaram pelos tempos imemoriais, deixando sua marca indelével na tapeçaria da história.
'''

def obter_descricao_tipo(tipo):
    #Tipos d Classe Feiticeiro; Elementos:
    if tipo == 1:
        return '''
        Elemento Ar
        
        Os Feiticeiros do Ar são mestres da manipulação etérea, capazes de invocar a magia astral para moldar o elemento do ar a seu favor. 
        Eles pertencem ao venerável Clã de Ar, um dos seis clãs elementais que dominam os aspectos mais puros da natureza.

        Habilidades:
        - Sussurro do Vento: Com um gesto, o Feiticeiro do Ar pode convocar uma brisa suave ou uma rajada violenta, usando-a para confundir e desorientar seus inimigos.
        - Voo Etéreo: Utilizando o poder do ar, esses feiticeiros podem levitar ou voar, escapando de perigos ou alcançando posições vantajosas.
        - Corte de Ar: Eles podem canalizar a fúria dos ventos, utilizando de armas ou das próprias mãos fazendo um movimento de corte, loançando um corte de vento na direção inimiga.

        Limitações:
        - **Concentração: A manipulação do ar requer foco intenso, e qualquer distração pode dissipar os feitiços.
        
        Resistência Elementar:
        - Resistência a Terra: Os Feiticeiros do Ar podem ser menos afetados por ataques baseados em terra, como deslizamentos de terra ou tremores, devido à sua habilidade de levitar ou voar.
        
        Clã de Ar:
        O Clã de Ar é conhecido por sua sabedoria e conexão profunda com o mundo espiritual. Eles valorizam o conhecimento e a liberdade acima de tudo, e seus feiticeiros são respeitados como guardiões do equilíbrio natural.
        '''
    
    elif tipo == 2:
        return '''
        Elemento Água
        
        Os Feiticeiros da Água são os sábios das marés, fluentes na linguagem fluida dos oceanos e rios. 
        Eles são membros do Clã de Água, um dos seis clãs elementais que tecem a essência dos elementos em magia palpável.

        Habilidades:
        - Fluxo Sereno: Com um aceno de mãos, o Feiticeiro da Água pode acalmar as águas agitadas ou convocar ondas para lavar os obstáculos.
        - Dança das Correntes: Eles podem manipular correntes aquáticas para criar vórtices ou propulsão, movendo-se rapidamente ou prendendo inimigos.
        - Pistola de Água: Os feiticeiros podem criar ou coletar gotas de água, disparando-as em alta velocidade como uma metralhadora, causando danos rápidos e contínuos.

        Limitações:
        - Consumo de Mana: A criação de água a partir do nada é uma habilidade poderosa que consome uma quantidade significativa de mana, limitando a frequência com que pode ser usada.
        - Temperatura: Extremos de calor ou frio podem afetar a eficácia dos feitiços, congelando ou evaporando a água.

        Resistência Elementar:
        - Resistência a Fogo: Os Feiticeiros da Água têm uma resistência natural contra o fogo, podendo extinguir chamas e resistir a altas temperaturas com facilidade.
        
        Clã de Água:
        O Clã de Água é conhecido por sua adaptabilidade e profundidade emocional. 
        Suas ações fluem de acordo com seus desejos, podendo ser selvagens e imparáveis como ondas descontroladas do mar ou calmos e serenos como o oceano. 
        São inconstantes e é impossível adivinhar sua próxima ação, tornando-os adversários formidáveis e aliados valiosos.
        '''
    
    elif tipo == 3:
        return '''
        Elemento Fogo
        
        Os Feiticeiros do Fogo são os arautos das chamas, tecendo a essência ardente do fogo em magia incandescente. 
        Eles são membros do Clã de Fogo, um dos seis clãs elementais que dominam o poder bruto e a paixão dos elementos.

        Habilidades:
        - Toque Incendiário: Com um simples toque, o Feiticeiro do Fogo pode incendiar objetos ou inimigos, usando o fogo como uma arma precisa.
        - Muralha de Chamas: Eles podem criar barreiras de fogo para proteção ou para cercar adversários, controlando o campo de batalha.
        - Chuva de Cinzas: Invocando o poder do fogo, esses feiticeiros podem fazer chover cinzas quentes, que queimam e desorientam os inimigos.

        Limitações:
        - Controle Emocional: A magia do fogo é intensamente ligada às emoções do feiticeiro. Raiva ou medo podem intensificar ou perder o controle das chamas.
        - Ambiente: Locais úmidos ou com pouca oxigenação podem limitar a eficácia dos feitiços de fogo.

        Resistência Elementar:
        - Resistência a Gelo: Os Feiticeiros do Fogo podem derreter ataques baseados em gelo e são imunes ao frio extremo, mantendo-se aquecidos mesmo em ambientes congelantes.
        
        Clã de Fogo:
        O Clã de Fogo é conhecido por sua intensidade e força de vontade. 
        Suas ações são impetuosas e poderosas, como uma erupção vulcânica, mas também podem ser inspiradoras e vivificantes, como o calor do sol nascente.
        '''
    
    elif tipo == 4:
        return '''
        Elemento Gelo
        
        Os Feiticeiros do Gelo são os conjuradores do inverno eterno, capazes de tecer a essência fria do gelo em magia cristalina. 
        Eles são membros do Clã de Gelo, um dos seis clãs elementais que dominam a serenidade e a precisão dos elementos.

        Habilidades:
        - Toque Congelante: Com um gesto, o Feiticeiro do Gelo pode cobrir objetos ou inimigos em camadas de gelo, imobilizando-os ou causando danos por congelamento.
        - Muralha de Gelo: Eles podem erguer barreiras sólidas de gelo para defesa ou para criar obstáculos estratégicos no campo de batalha.
        - Tempestade de Neve: Invocando o poder do gelo, esses feiticeiros podem desencadear uma tempestade de neve cegante, dificultando a visão dos inimigos e reduzindo sua mobilidade.

        Limitações:
        - Condições Ambientais: A eficácia da magia de gelo pode ser afetada por condições ambientais quentes, que podem derreter o gelo rapidamente.
        - Equilíbrio: O uso excessivo da magia de gelo pode levar a um desequilíbrio, tornando o feiticeiro vulnerável a ataques enquanto recupera seu equilíbrio mágico.
        
        Resistência Elementar:
        - Resistência a Água: Os Feiticeiros do Gelo podem congelar a água e são resistentes a ataques baseados em água, como ondas ou correntes.
        
        Clã de Gelo:
        O Clã de Gelo é conhecido por sua calma e controle. 
        Suas ações são calculadas e metódicas, como a formação lenta de cristais de gelo, mas quando provocados, podem ser impiedosos e devastadores como uma avalanche.
        '''
    
    elif tipo == 5:
        return '''
        Elemento Raio
        
        Os Feiticeiros do Raio são os mestres da eletricidade, canalizando a energia volátil do raio em magia pulsante. 
        Eles são membros do Clã de Raio, um dos seis clãs elementais que dominam a velocidade e o impacto dos elementos.

        Habilidades:
        - Toque Eletrizante: Com um movimento rápido, o Feiticeiro do Raio pode liberar uma descarga elétrica, paralisando ou causando danos elétricos aos inimigos.
        - Escudo de Plasma: Eles podem gerar um campo de força de energia elétrica para se defender ou interromper ataques inimigos.
        - Lâmina de Raios: Invocando o poder do raio, esses feiticeiros podem criar lâminas de energia que cortam e queimam com precisão letal.

        Limitações:
        - Condução: A presença de materiais condutores ou a falta deles pode afetar a eficácia dos feitiços de raio.
        - Desgaste: O uso contínuo da magia de raio pode causar fadiga, exigindo períodos de descanso para recarregar as energias.
        
        Resistência Elementar:
        - Resistência a Ar: Os Feiticeiros do Raio são menos suscetíveis a danos causados por ataques de ar, pois podem dissipar correntes de vento com suas descargas elétricas.
        
        Clã de Raio:
        O Clã de Raio é conhecido por sua agilidade e decisão. 
        Influenciados pela cultura japonesa, eles valorizam a honra e a precisão, como um samurai que desfere um golpe rápido e certeiro. 
        Suas ações são imprevisíveis e rápidas, como um relâmpago que rasga o céu sem aviso.
        '''
    
    elif tipo == 6:
        return '''
        Elemento Terra
        
        Os Feiticeiros da Terra são os guardiões da solidez, mestres na arte de moldar a terra e a pedra em magia tangível. 
        Eles são membros do Clã de Terra, um dos seis clãs elementais que comandam a estabilidade e a resiliência dos elementos.

        Habilidades:
        - Punho de Pedra: Com um comando firme, o Feiticeiro da Terra pode fazer com que a terra se levante para formar punhos gigantes, capazes de esmagar obstáculos ou inimigos.
        - Escudo Terrano: Eles podem convocar paredes de terra para proteção imediata ou para alterar o terreno ao seu redor.
        - Tremor: Invocando o poder da terra, esses feiticeiros podem causar tremores localizados, desestabilizando adversários e estruturas.

        Limitações:
        - Mobilidade: A magia da terra muitas vezes requer contato com o solo, o que pode limitar a mobilidade do feiticeiro em ambientes onde a terra não está presente.
        - Velocidade de Conjuração: Os feitiços de terra podem ser poderosos, mas geralmente são mais lentos para conjurar, exigindo planejamento e tempo.
        
        Resistência Elementar:
        - Resistência a Raio: Os Feiticeiros da Terra podem usar o solo para se aterrar, reduzindo significativamente o impacto de ataques elétricos.
        
        Clã de Terra:
        O Clã de Terra é conhecido por sua paciência e determinação. 
        Suas ações são firmes e deliberadas, como as antigas montanhas que resistem ao teste do tempo. 
        Eles são a personificação da força tranquila, mas quando provocados, sua fúria pode ser tão avassaladora quanto um deslizamento de terra.
        '''
    
    #Tipos da Classe de Caçador; Armas:
    elif tipo == 11:
        return '''
        Uma Dupla de Pistolas
        
        As Duplas de Pistolas dos Caçadores são armas mágicas de precisão letal, cada uma incrustada com runas interdimensionais que acessam um depósito de munição variada.
        Os cartuchos podem ser carregados com balas de madeira, ferro, prata, entre outros materiais, cada um com propriedades específicas para combater monstros e humanos ameaçadores.

        Mecanismo:
        - Tambor Rotativo: Para alternar entre os diferentes tipos de munição, o caçador gira o tambor da pistola, selecionando a bala desejada para o próximo disparo.
        - Pólvora Encantada: A pólvora dentro de cada cartucho é encantada para dobrar a velocidade do disparo, garantindo que cada tiro atinja seu alvo com uma rapidez surpreendente.
        - Material: As pistolas são forjadas a partir do metal mais resistente e leve disponível, tornando-as armas duráveis e fáceis de manusear em combate.

        Características Únicas:
        - Modelo Exclusivo: Cada Dupla de Pistolas é única, com 'cópias' inferiores sendo vendidas a preços exorbitantes no mercado negro,
        tentando imitar, sem sucesso, a superioridade das originais.

        Uso em Combate:
        Os Caçadores utilizam essas pistolas com maestria, combinando sua habilidade marcial com a magia inerente às armas para executar disparos que são tão precisos quanto mortais.
        A versatilidade das munições permite que se adaptem rapidamente a qualquer ameaça, tornando-os adversários temíveis para qualquer criatura das sombras.
                '''
    
    elif tipo == 12:
        return '''
        Arco e Flecha Enfeitiçados
        
        Os Arco e Flecha Enfeitiçados são manifestações mágicas de combate à distância, nascidos de uma dupla de anéis encantados usados pelos Caçadores. 
        Ao canalizar uma fração de sua mana, um arco de energia esverdeada e élfica emerge de um anel, enquanto o outro materializa flechas da mesma essência.

        Mecanismo:
        - Anéis Mágicos: Os anéis funcionam como catalisadores, permitindo que o Caçador crie instantaneamente o arco e as flechas necessárias para o combate.
        - Rubis Registradores: Quando o Caçador atinge um alvo com um soco usando os anéis, os rubis incrustados registram a mana do alvo, permitindo que as flechas subsequentemente disparadas sejam teleguiadas até o mesmo.
        - Absorção de Mana Astral: Embora os anéis consumam uma pequena porção da mana do Caçador, eles primariamente absorvem mana astral do ambiente, garantindo que o Caçador não seja rapidamente esgotado.

        Uso em Combate:
        - Nascentes Mágicas: O uso dos anéis é otimizado em locais ricos em mana, como nascentes mágicas, onde a abundância de energia astral torna o processo de criação do arco e das flechas mais eficiente.
        - Itens Únicos: Inspirados na lendária Espada de Thorfeus, esses anéis são peças únicas no mundo, conferindo aos Caçadores uma vantagem única e poderosa no campo de batalha.

        Os Caçadores empregam esses arcos e flechas enfeitiçados com destreza, combinando sua habilidade marcial com a magia dos anéis para ataques precisos e mortais.
        A capacidade de teleguiar as flechas os torna caçadores implacáveis, capazes de rastrear e eliminar ameaças com eficácia incomparável.
                '''
    
    elif tipo == 13:
        return '''
        Espada Mística
        
        A Espada Mística de Thorfeus, conhecida como Excalibur, é uma relíquia antiga envolta em lendas. 
        Esta espada possui a capacidade única de absorver qualquer tipo de magia, seja Astral ou Caos, e transformar essa energia em ataques devastadores graças as runas em sua lâmina.

        Habilidades:
        - Reflexão Mágica: Excalibur pode refletir feitiços lançados contra ela, virando a ofensiva do inimigo contra ele mesmo.
        - Absorção de Mana: A espada permite que seu usuário digno absorva a mana ou feitiços absorvidos, potencializando suas próprias habilidades mágicas.
        - Chamado da Espada: Quando seu nome é invocado, Excalibur responde ao chamado, flutuando até a mão de seu verdadeiro dono, escolhido pela própria espada.

        Características Únicas:
        - Lâmina Eterna: A lâmina de Excalibur é mais afiada do que qualquer outra já forjada, mantendo seu fio eternamente sem necessidade de afiação.
        - Vínculo com o Portador: A espada avalia a dignidade de quem a empunha, podendo absorver uma quantidade excessiva de mana do portador se considerado indigno.

        Uso em Combate:
        Excalibur é uma arma de poder incomparável, ideal para os Caçadores que enfrentam as mais terríveis Criaturas Místicas Malignas. 
        Sua presença em batalha é um símbolo de esperança e força, inspirando aliados e intimidando adversários com sua aura mística.
        '''
    
    elif tipo == 14:
        return '''
        Foice do Purgatório
        
        A Foice do Purgatório é uma arma temida, originária da prisão Divinus, usada para executar os mais perigosos detentos. 
        Esta foice não apenas corta a carne, mas também a alma, enviando a existência do ser cortado para o vazio, um destino pior do que a morte.

        Habilidades:
        - Corte da Alma: Um golpe da Foice do Purgatório é capaz de separar a alma do corpo, aniquilando completamente a existência do alvo.
        - Transformação: Quando inativa, a foice se disfarça como um bastão longo e negro. Ao ser ativada, duas lâminas de energia surgem em suas pontas, uma maior que a outra, refletindo a cor da mana do portador.
        - Onda Cortante: Cada corte libera uma onda de energia cortante que se estende por metros, capaz de devastar múltiplos inimigos em seu caminho.

        Características Únicas:
        - Cabo Prolongado: O cabo preto e estendido da foice permite um alcance excepcional, dando ao Caçador a vantagem em combates à distância.
        - Eco do Vazio: Aqueles cortados pela Foice do Purgatório não encontram repouso após a morte; suas almas são apagadas, deixando um rastro de desespero entre aqueles que testemunham seu poder.

        Uso em Combate:
        Os Caçadores empregam a Foice do Purgatório com respeito e cautela, cientes de seu poder destrutivo. Em suas mãos, torna-se uma ferramenta de justiça, erradicando as ameaças que assolam os reinos com uma eficiência sombria.
        '''
    
    elif tipo == 15:
        return '''
        Correntes da Justiça
        
        As Correntes da Justiça são um par de braceletes mágicos ligados a cinco anéis, formando uma luva de metal que se estende em correntes letais. 
        Cada elo é forjado com precisão, terminando em pontas afiadas capazes de perfurar até mesmo as armaduras mais resistentes.

        Mecanismo:
        - Extensão e Movimento: As correntes são incrivelmente versáteis, podendo se esticar e se mover conforme a vontade do Caçador, permitindo ataques surpresa e manobras defensivas.
        - Luvas de Combate: Quando não estão estendidas, as correntes repousam como braceletes, prontas para serem ativadas em um instante.

        Características Únicas:
        - Adaptação Mágica: As correntes se adaptam à mana do usuário, tornando-se uma extensão de sua vontade e estilo de combate.
        - Poder Perfurante: As pontas perfurantes das correntes são projetadas para penetrar não apenas a carne, mas também as barreiras mágicas, tornando-as armas ideais contra uma variedade de ameaças.

        Uso em Combate:
        Os Caçadores utilizam as Correntes da Justiça com maestria, controlando o campo de batalha com sua habilidade de atacar e defender de múltiplos ângulos. 
        A capacidade de estender e manipular as correntes torna os Caçadores adversários imprevisíveis e formidáveis.
        '''
    
    #Tipos da Classe de Bruxo; Caos:
    elif tipo == 21:
        return '''
        Sombras
        
        Os Bruxos do Caos especializados na Magia da Sombra são mestres do oculto e do intangível. 
        Eles manipulam as sombras como extensões de si mesmos, criando ilusões, escondendo-se da vista ou mesmo tocando a mente de suas vítimas com um frio paralisante.

        Habilidades:
        - Manto das Trevas: Capaz de envolver-se em sombras, o bruxo torna-se invisível aos olhos dos incautos.
        - Garras Sombrias: Invoca garras feitas de pura escuridão, capazes de rasgar a carne e a essência espiritual.
        '''
    
    elif tipo == 22:
        return '''
        Insetos
        
        A Magia dos Insetos permite que os Bruxos do Caos convoquem e controlem insetos de todas as formas e tamanhos. 
        Esses insetos podem ser usados para espionagem, como vetores de venenos mortais ou como um enxame devorador.

        Habilidades:
        - Enxame Voraz: Libera um enxame de insetos que consome tudo em seu caminho.
        - Sussurro dos Insetos: Permite comunicação e controle sobre insetos, utilizando-os como espiões ou mensageiros.
        '''
    
    elif tipo == 23:
        return '''
        Sangue
        
        Os praticantes da Magia do Sangue manipulam a própria essência da vida. Eles podem curar feridas, controlar seres vivos através de seu sangue ou extrair a força vital de suas vítimas.

        Habilidades:
        - Controle Hemático: Domina a vontade de criaturas vivas ao manipular seu sangue.
        - Exsanguinação: Drena a energia vital de um ser, enfraquecendo-o ou até mesmo matando-o.
        '''
    
    elif tipo == 24:
        return '''
        Ossos
        
        Os Bruxos do Caos que dominam a Magia dos Ossos possuem o poder de manipular e reformar o esqueleto de seus próprios corpos. 
        Eles podem moldar seus ossos para criar armas, defesas ou até mesmo novas formas corpóreas, exibindo uma maestria sobre a própria anatomia que desafia os limites da biologia.

        Habilidades:
        - Armas Ósseas: Podem projetar lâminas, lanças e outras formas de armas diretamente de seus ossos, tornando cada parte de seu corpo um potencial instrumento de combate.
        - Defesa Esquelética: Capazes de engrossar e fortalecer seus ossos, criam uma armadura natural impenetrável.
        - Manipulação Óssea: Com controle total sobre sua estrutura óssea, podem estender, retrair ou remodelar seus ossos para adaptar-se a qualquer situação de combate.
        - Regeneração Óssea: Mesmo após sofrerem danos, têm a habilidade de reconstituir e curar seus ossos, mantendo a integridade física em meio à batalha.

        Uso em Combate:
        Os Bruxos do Caos utilizam a Magia dos Ossos com uma combinação de brutalidade e graça artística. 
        Eles são adversários formidáveis que podem surpreender seus inimigos com a versatilidade e a resiliência que essa magia proporciona.
        '''
    
    #Tipos da Classe Criatura; Espécies:
    elif tipo == 31:
        return '''
        Dragão
        
        Os Dragões são as criaturas de Rank SS, as mais majestosas e poderosas do mundo mágico. 
        Com sua imponente presença, eles encarnam a força bruta e a sabedoria ancestral.

        Características:
        - Voo Majestoso: Com suas vastas asas, os Dragões dominam os céus, exibindo uma liberdade que poucas criaturas podem igualar.
        - Sopro de Fogo: Uma das habilidades mais temidas dos Dragões é sua capacidade de expelir chamas devastadoras, capazes de derreter aço e pedra.
        - Intelecto Superior: Dragões possuem uma inteligência aguçada, muitas vezes superando a dos seres humanos em astúcia e conhecimento.

        Habilidades Mágicas:
        - Manipulação Elemental: Além do fogo, alguns Dragões podem controlar outros elementos, como gelo, trovão ou mesmo magia arcana.
        - Cura Regenerativa: Dragões têm uma taxa de cura incrivelmente rápida, permitindo-lhes recuperar-se de ferimentos que seriam fatais para outras criaturas.

        Papel no Mundo Mágico:
        Os Dragões são frequentemente vistos como guardiões de tesouros imensuráveis e detentores de segredos antigos. 
        Sua presença impõe respeito e admiração, e muitas vezes, eles são o centro de histórias e lendas passadas através das gerações.
        '''
    
    elif tipo == 32:
        return '''
        Vampiro
        
        Os Vampiros de Rank S são entidades sobrenaturais de poder e graça inigualáveis. 
        Eles personificam a noite e exibem habilidades que transcendem as capacidades humanas.

        Características:
        - Força, Velocidade e Resistência: Possuem atributos físicos que superam em muito os dos seres humanos, tornando-os predadores natos.
        - Sentidos Aguçados: Seus seis sentidos são extraordinariamente desenvolvidos, permitindo-lhes ouvir o pulsar do sangue nas veias e rastrear presas pelo cheiro.
        - Hipnose: Com seus olhos vampirinos podem hipnotizar seres não-mágicos como quiser, principalmente se for uma vampiro forte.

        Alimentação:
        - Dieta Hematófaga: Se alimentam de sangue para sustentar sua força e longevidade, com uma predileção especial pelo sangue humano, que consideram um manjar.

        Fraquezas:
        - Luz Solar: São vulneráveis à luz do sol, o que os restringe ao manto da noite.
        - Imortalidade Condicional: Embora imortais, podem ser mortos por decapitação, destruição do coração ou incineração.

        Habilidades de Cura:
        - Regeneração Acelerada: Curam feridas a uma velocidade surpreendente, especialmente após a ingestão de sangue.

        Transformações:
        - Caninos Afiados: Podem manifestar caninos extremamente afiados à vontade, preparando-se para o ataque.
        - Olhos Predatórios: Seus olhos assumem um aspecto aterrorizante com fundo preto e pupilas vermelhas durante a caça ou combate.

        Os Vampiros de Rank S são temidos e respeitados em igual medida, sendo criaturas de grande poder dentro da classe Criatura. Sua existência é um testemunho da magia antiga que ainda permeia o mundo.
        '''
    
    elif tipo == 33:
        return '''
        Lobisomem

        Os Lobisomens são criaturas metamórficas que transitam entre a forma humana e sua verdadeira natureza bestial. 
        Na forma humana, já são seres de grande força, agilidade e resistência, mas é na forma de lobisomem que seu poder atinge o ápice.

        Características:
        - Transformação: Podem voluntariamente mudar para a forma de lobisomem, aumentando exponencialmente sua força e velocidade.
        - Visão Noturna: Possuem a capacidade de enxergar claramente no escuro, o que os torna caçadores noturnos implacáveis.
        - Sentidos Aguçados: Todos os seus sentidos são extremamente desenvolvidos, permitindo-lhes rastrear presas e perceber perigos com facilidade.

        Habilidades Físicas:
        - Garras e Caninos: Suas garras e dentes são armas naturais, fortes o suficiente para rasgar a maioria dos materiais.
        - Cura Acelerada: Apresentam uma habilidade de cura rápida, que é ainda mais potencializada pelo consumo de carne.

        Vulnerabilidades:
        - Lua Cheia: São compelidos a se transformar durante a lua cheia, perdendo o controle sobre suas ações.
        - Mortalidade: Apesar de sua resistência física excepcional, não são imortais e podem ser mortos, embora seja uma tarefa difícil.

        Os Lobisomens de Rank A são temidos por sua ferocidade e respeitados por sua nobreza. 
        Eles caminham na linha tênue entre humano e monstro, desempenhando um papel complexo no equilíbrio dos reinos mágicos.
                '''
    
    elif tipo == 34:
        return '''
        Minotauro
        
        Os Minotauros são seres imponentes que transitam entre a forma humana e a forma de Minotauro à vontade. 
        Quando transformados, tornam-se gigantes de força e resistência extraordinárias.

        Características:
        - Transformação: Podem mudar para a forma de Minotauro, crescendo até 2 metros de altura e ganhando uma musculatura robusta.
        - Aparência Física: Do peito para cima, adquirem pelos e uma cabeça de minotauro com chifres afiados e resistentes, enquanto suas mãos se assemelham a cascos.

        Habilidades Físicas:
        - Força Sobrehumana: Mesmo não sendo tão ágeis quanto lobisomens ou vampiros, possuem uma força descomunal.
        - Resistência Superior: Sua constituição física lhes confere uma resistência muito acima da média, tornando-os adversários duráveis em combate.

        Sentidos Aguçados:
        - Visão Vermelha: Com uma visão especial, são capazes de detectar seres vivos pelo fluxo sanguíneo, mesmo que ocultos.
        - Olfato Excepcional: Seu olfato é incrivelmente desenvolvido, permitindo-lhes rastrear presas e perigos com facilidade.

        Os Minotauros de Rank B são respeitados por sua força bruta e capacidade de resistir a danos significativos. 
        Eles são uma força a ser reconhecida nos reinos mágicos, trazendo uma combinação única de poder e percepção sensorial para qualquer confronto.
        '''
    
    elif tipo == 35:
        return '''
        Sereia
        
        As Sereias, juntamente com seus equivalentes masculinos, os Tritões, são as soberanas dos mares. 
        Embora classificadas como Rank C devido à sua dependência do oceano, suas habilidades aquáticas são incomparáveis.

        Características:
        - Dependência Aquática: Suas habilidades são maximizadas na água, onde se sentem em casa. Em terra, sofrem de náuseas e tonturas após algumas horas.
        - Atributos Físicos: Em terra, possuem força, velocidade, agilidade, resistência e cura sobrehumanas, mas não ao nível de criaturas de Rank superior.
        - Mestres Nadadores: No mar, nadam com uma velocidade inatingível pelos melhores equipamentos humanos.

        Comunicação e Controle:
        - Domínio Marinho: Comunicam-se e, em muitos casos, comandam seres marinhos, que as obedecem se forem amigáveis ou as reconhecerem como superiores.

        Habilidades de Caça:
        - Unhas Afiadas: Tanto em terra quanto no mar, suas unhas podem crescer e se tornar tão afiadas quanto as presas mais mortais, permitindo-lhes caçar e matar eficientemente.
        - Cauda de Sereia: A parte inferior de seu corpo é composta por uma cauda de nadadeira bela e resistente, que pode ser usada como arma debaixo d'água.

        Aparência e Canto:
        - Beleza Hipnótica: Acima da cintura, têm a aparência de mulheres lindas e atraentes, com uma variedade de cores de pele.
        - Canto Ilusório: Seu canto é capaz de atrair e hipnotizar homens e mulheres, levando-os para as profundezas do mar. O efeito do canto varia no cérebro humano.

        Poderes Coletivos:
        - Criação de Maremotos: Quando reunidas, as Sereias têm o poder de criar maremotos, demonstrando sua conexão profunda e poderosa com o oceano.

        As Sereias são criaturas de beleza e poder, cuja presença nos mares é tanto uma bênção quanto um perigo para aqueles que se aventuram em suas águas.
        '''
    
    elif tipo == 36:
        return '''
        Harpia
        
        As Harpias são criaturas de beleza letal, metade mulher e metade ave, capazes de transformar-se de sua forma humana para a forma de Harpia. 
        Embora classificadas como Rank D, suas habilidades são notáveis.

        Características:
        - Transformação: Podem alternar entre a forma humana e a forma de Harpia, adotando características físicas avianas.
        - Força e Resistência: Comparáveis a um humano forte e bem treinado, mas não possuem imortalidade.
        
        Habilidades de Voo:
        - Asas Penosas: Possuem asas que se estendem do pulso até a costela, permitindo-lhes voar a alturas e velocidades impressionantes.
        - Agilidade Aérea: Voam mais rápido do que qualquer ave não-mágica, dominando os céus com sua presença.
        - Asas Poderosas: As asas das Harpias, além de permitirem voo de alta velocidade, são extremamente fortes, capazes de gerar ventos poderosos ao serem batidas.
        - Criação de Tornados: Quando em grupo, as Harpias podem combinar suas forças para criar tornados, demonstrando seu domínio sobre os ventos e o clima.
        
        Atributos Físicos:
        - Visão Aguçada: Na forma de Harpia, têm uma visão excepcional, capaz de detectar presas a quilômetros de distância.
        - Garras Afiadas: Seus dedos transformam-se em garras afiadas como aço, tornando-as caçadoras mortais.
        - Caninos Afiados: Seus caninos também se tornam mais afiados, complementando suas armas naturais.
        - Corpo Humano: Com corpos e peso humanos, suas asas precisam ser robustas para sustentar o voo, o que também lhes confere a capacidade de manipular correntes de ar com facilidade.

        As Harpias são criaturas de grande beleza e habilidade, cujas capacidades aéreas as tornam únicas entre as espécies mágicas. 
        Sua capacidade de causar tornados as coloca como seres respeitáveis e temidos quando em bando.
                '''
    
    elif tipo == 37:
        return '''
        Grifo Imperador das Trevas
        
        Os Grifos Imperadores das Trevas são as criaturas supremas dos céus e da terra, rivalizando em poder e majestade até mesmo com os Dragões.

        Características:
        - Penagem Escura: Ostentam uma plumagem negra e pelagem cinzenta, simbolizando sua nobreza e poder.
        - Cauda Majestosa: Possuem uma cauda longa e robusta, que reflete sua elegância e status elevado.

        Habilidades Físicas:
        - Asas Imponentes: Suas asas vastas e fortes garantem um voo de velocidade incomparável, tornando-os as criaturas mais rápidas dos céus.
        - Garras Afiadas: Equipados com garras letais tanto nas patas dianteiras de águia quanto nas traseiras de leão, são capazes de perfurar corpos com facilidade.

        Atributos Sobrenaturais:
        - Força, Agilidade e Resistência: Exibem uma força e agilidade extraordinárias, com uma resistência formidável e uma capacidade de cura acelerada.
        - Sentidos Desenvolvidos: Todos os seus sentidos são extremamente apurados, e seu olhar penetrante pode enxergar a quilômetros de distância e no mais profundo escuro.

        Domínio e Comando:
        - Imperadores Naturais: Como líderes natos, os Grifos Imperadores das Trevas comandam as outras sub-espécies de grifos, leões e aves, exercendo domínio tanto nos ares quanto na terra.

        Os Grifos Imperadores das Trevas são seres de uma linhagem antiga e poderosa, cuja presença impõe respeito e admiração em todos os reinos mágicos.
        '''
    
#Função de escolha de Classe
def classe_jogador():
    while True:
        classe_escolhida = obter_escolha('''
        Escolha uma das opções digitando seus respectivos números:
        [1] Feiticeiro
        [2] Caçador
        [3] Bruxa/Bruxo do Caos
        [4] Criatura
       
        Digite o número da opção escolhida: ''', [1, 2, 3, 4])

        print(f"\n=== Classe {classe_info[classe_escolhida]} escolhida. ===")
        if ler_descricao_classe(classe_escolhida):
            print(obter_descricao_classe(classe_escolhida))
        else:
            print("Descrição da classe ignorada.")

        return classe_escolhida

#Função de escolha de Tipo, de acordo com a Classe
def obter_tipo(classe):
    if classe == 1:
        while True:
            tipo_escolhido = obter_escolha('''Qual elemento de mana você manipula?
            [1] Ar
            [2] Água
            [3] Fogo
            [4] Gelo
            [5] Raio
            [6] Terra

            Digite o número da opção escolhida: ''', [1, 2, 3, 4, 5, 6])
            
            print(f"\n=== Elemento {elementos[tipo_escolhido]} escolhido. ===")
            if ler_descricao_tipo(tipo_escolhido):
                print(obter_descricao_tipo(tipo_escolhido))
            else:
                print("Descrição do elemento ignorada.")

            return tipo_escolhido
            
    elif classe == 2:
        while True:
            tipo_escolhido = obter_escolha('''Qual arma encantada você manipula?
            [11] Uma Dupla de Pistolas
            [12] Arco e Flecha Enfeitiçados
            [13] Espada Mística
            [14] Foice do Purgatório
            [15] Correntes da Justiça
            
            Digite o número da opção escolhida: ''', [11, 12, 13, 14, 15])
            
            print(f"\n=== Arma {armas[tipo_escolhido]} escolhida. ===")
            if ler_descricao_tipo(tipo_escolhido):
                print(obter_descricao_tipo(tipo_escolhido))
            else:
                print("Descrição da arma ignorada.")

            return tipo_escolhido
            
    elif classe == 3:
        while True:
            tipo_escolhido = obter_escolha('''Qual especialidade de Caos você manipula? 
            [21] Sombras
            [22] Insetos
            [23] Sangue
            [24] Ossos
                
            Digite o número da opção escolhida: ''', [21, 22, 23, 24])
            
            print(f"\n=== Caos {caos[tipo_escolhido]} escolhido. ===")
            if ler_descricao_tipo(tipo_escolhido):
                print(obter_descricao_tipo(tipo_escolhido))
            else:
                print("Descrição do caos ignorado.")

            return tipo_escolhido
            
    elif classe == 4:
        while True:
            tipo_escolhido = obter_escolha(f'''
            [31] Dragão
            [32] Vampiro
            [33] Lobisomem
            [34] Minotauro
            [35] Sereia
            [36] Harpia
            [37] Grifo
            
            Digite o número da opção escolhida: ''', [31, 32, 33, 34, 35, 36, 37])
            
            print(f"\n=== Criatura {criaturas[tipo_escolhido]} escolhida. ===")
            if ler_descricao_tipo(tipo_escolhido):
                print(obter_descricao_tipo(tipo_escolhido))
            else:
                print("Descrição da criatura ignorada.")

            return tipo_escolhido
            
    else:
        return None  # Retorna None se a classe não estiver entre 1 e 4

#Função Main / Principal Código
def main():
    bem_vindo()
    classe = classe_jogador()
    tipo = obter_tipo(classe)

    if classe == 1:
        print(f"\n==== Um {classe_info[classe]} que manipula o elemento {elementos[tipo]}. ====")
    elif classe == 2:
        print(f"\n==== Um {classe_info[classe]} que manipula {armas[tipo]}. ====")
    elif classe == 3:
        print(f"\n==== Um {classe_info[classe]} que manipula {caos[tipo]}. ====")
    elif classe == 4:
        print(f"\n==== Uma {classe_info[classe]} da espécie {criaturas[tipo]}. ====")

    nome = input("\nPor último, digite seu nome, combatente: ")
    print(f"\n\nCombatente:\n{nome}\n{classe_info[classe]}")
    if classe == 1:
        print(f"Manipula {elementos[tipo]}")
    elif classe == 2:
        print(f"Usa {armas[tipo]}")
    elif classe == 3:
        print(f"Manipula {caos[tipo]}")
    elif classe == 4:
        print(f"Da Espécie {criaturas[tipo]}")
    print("\nPronto para o duelo!")

#Execução
if __name__ == "__main__":
    main()

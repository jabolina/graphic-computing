# Simple MS-Paint clone

From the description, the user must be able to choose from a palette with at least 16 colors,
can draw a line, rectangle, square, circle, polyline and curves (Bezier or Spline), and also
have a fill tool.

The draw routine must implement Bresenham algorithm and middle point algorithm for circles.

### Done ###

- [ ] GUI
    - [X] Line
    - [X] Circle
    - [X] Square
    - [ ] Polyline
    - [X] Rectangle
    - [X] Curve(Bezier)
- [X] Bresenham algorithm
- [X] Middle point algorithm


#### Notas ####

No momento, não tem como o usuário meio que "interagir" igual no paint, pois aqui ele só escolhe os
pontos e o desenho faz, não tem como ele editar, isso acontece porque cada desenho é feito somente uma vez
na Surface do pygame, se for necessesário fazer com essa interação (só perfumaria), tudo na tela tem que
ser redesenhado a cada tick do clock. Assim, toda vez que algo novo for desenhado na tela teriamos que salvar
esse contexto, porque a cada tick do clock desenhariamos as coisas padrões (opções, cores) e depois viriamos desenhado
as coisas salvas no contexto.

A parte ruim, é que quanto mais coisas desenhadas, mais pesado o contexto vai ficar e assim mais lento ainda.

Uma das maneiras de salvar assim, seria no contexto conter um array de objetos, que possue a Surface referente ao
desenho, com alpha 100, para ser transparente, juntamente com a posição na tela (x, y), assim seria só força
as surfaces na tela, em vez de desenhar tudo novamente.
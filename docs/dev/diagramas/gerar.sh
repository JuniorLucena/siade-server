#!/bin/sh
echo "Gerando diagramas"
dot -Tpng casos_de_uso.dot -o casos_de_uso.png
dot -Tpng classes.dot -o classes.png
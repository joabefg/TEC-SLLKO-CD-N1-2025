## Data 
- 3 jan 2006 - 27 maio 2015

## Markdown
- Create new Text
- Inserir "Visualização de Preços de Casas US 2005-2015"

## Mapa
- Create new Map
- Layers > Add Layer > Choropleph
- Layer: USA Zip Code
- Join Field: Postal Code
- Index Pattern: Casas USA
- Join Field: Zip Code
- Add Layer

## Registros por data
- Line
- hax: DocumentDate
- vax: Count

## Categoria Material Construção
- Bar Vertical
- hax: BldgGrade
- vax: Count

## Tipo Propriedade
- Donut
- Slice: PropertyType
- Size: Count

## Novas Construções
- Pie
- Slice: New Construction
- Size: Count

## Tamanho por data
- Line
- hax: YrBuilt
- vax: Avg SqFtToLiving

## Preços/Tamanhos por Zona/Bairros
- Table
- Rw: ZipCode
- Mt: Avg AdjSalePrice (Sort Descending)
- Mt: Avg SqFtToLiving
- Mt: Count
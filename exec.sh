## Args order:
# points_number
# temporal_component
# start_timestamp
# end_timestamp
# shapefile

# read -p "Insira o número de pontos desejado: " points_number
points_number=10
temporal_component=120
shapefile="../files/BRA_shp.zip"
program="generator.py"
start_timestamp=1719304546
end_timestamp=1719701874

python3 $program $points_number $temporal_component $start_timestamp $end_timestamp $shapefile


-- SQL script that lists all bands with Glam rock as their main style, ranked by their longevity
SELECT band_name, (IFNULL(split, 2022) - formed) AS lifespan FROM metal_bands WHERE FIND_IN_SET('Glam rock', iFNULL(style, '')) > 0 ORDER BY lifespan DESC;

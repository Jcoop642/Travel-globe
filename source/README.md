# Travel Globe: how the page is built

`index.html` at the top of this branch is the whole globe in one file. It is built from the files in this folder.

- `template.html`: the page (layout, styles, map code) with three slots for the map library, the places and the layer colours.
- `places-seed.json`: the places list (copied from the Obsidian vault's Travel Globe room, Archive folder).
- `build.py`: fills the slots and writes the finished page.

## Rebuild

```
npm pack maplibre-gl@5.24.0 && tar xzf maplibre-gl-5.24.0.tgz
python3 source/build.py source/template.html source/places-seed.json package/dist/maplibre-gl.js package/dist/maplibre-gl.css index.html
```

Then bump the `VER` line in `template.html`, commit and push to `gh-pages`. The site updates about a minute later.

## Map sources

- Satellite imagery: Esri World Imagery (open tile address for now; a registered key is planned before the link is shared widely).
- Roads and names: OpenFreeMap vector tiles (OpenMapTiles schema, OpenStreetMap data).
- Terrain: Mapzen terrain tiles on AWS.
- Stand-in if Esri can't be reached: Sentinel-2 cloudless 2024 by EOX.

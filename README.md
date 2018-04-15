# Blender_ExportPathToSVG
Blender plugin for export strokes(mesh edges and path data) to svg.


## 概要
- シーン内のストロークをSVGにエクスポートします。
  - メッシュデータの各エッジをSegmentとして出力。
  - カーブデータの各SplineをPolylineとして出力。
- Freestyle SVG Exporter との違い
  - 各ストロークのサイズが、指定した単位系の実寸で出力します。
  - Blender内のオブジェクト単位でストロークをグループにして出力します。

## インストール
- installer/SVGPathExporter.zip  
  を設定ダイアログからインストールしてください。

## 使い方
- メニュ File > Export > Export strokes to SVG  
  を実行。

## オプション
- Select only
  - 選択された要素のみ出力。
- Unit
  - 出力するデータの単位系。
- Coordinate
  - 2Dに投影刷る座標系。
- Stroke width
  - ストロークの太さ  
    ※ 各ストロークに対して太さを設定することはできません。

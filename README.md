# WFiIS-Graph-Theory

One of the features of the IGraph package doesn't work. To run our project you need to make two changes. Find your Python IGraph drawing directory (e.g. C:\Users\usr\AppData\Local\Programs\Python\Python39\Lib\site-packages\igraph\drawing) and in file edge.py edit:

line 131 to:
             def get_label_position(self, edge, src_vertex, dest_vertex, curvature):

lines 159-162 
        if curvature:
            (x1, y1), (x2, y2) = src_vertex.position, dest_vertex.position
            aux1, aux2 = get_bezier_control_points_for_curved_edge(x1, y1, x2, y2, curvature)
            pos = evaluate_cubic_bezier_curve(x1, y1, *aux1, *aux2, x2, y2, .5)

in file graph.py
lines 489-491
            (x, y), (halign, valign) = edge_drawer.get_label_position(
                edge, src_vertex, dest_vertex, kwds.get("edge_curved")
            )

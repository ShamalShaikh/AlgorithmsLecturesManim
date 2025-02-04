from manim import *

class IntroScene(Scene):
    def construct(self):
        # Main title with favorite topic emphasis
        title = Text("Graph Theory", font_size=72).set_color(BLUE)
        subtitle = VGroup(
            Text("One of my favorite topics in CS", font_size=36),
            Text("A Computer Science perspective", font_size=32),
            Text("(Not focusing on mathematical proofs)", font_size=28)
        ).arrange(DOWN, buff=0.3)
        
        subtitle.next_to(title, DOWN, buff=1)
        
        # Key points about graph theory
        key_points = VGroup(
            Text("• Awesome algorithms", font_size=32),
            Text("• Very diverse field", font_size=32),
            Text("• Huge real-world applications", font_size=32),
            Text("• Algorithm implementation details", font_size=32)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        
        key_points.next_to(subtitle, DOWN, buff=1)
        
        # Animation sequence
        self.play(Write(title))
        self.wait(0.5)
        self.play(FadeIn(subtitle[0]))
        self.wait(0.5)
        self.play(FadeIn(subtitle[1:]))
        self.wait(1)
        self.play(
            LaggedStartMap(FadeIn, key_points, lag_ratio=0.5)
        )
        self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects])

class GraphTypesOverview(Scene):
    def construct(self):
        # Title
        title = Text("Types of Graphs", font_size=48).to_edge(UP)
        
        # Create sections for different graph types
        types_A = VGroup(
            Text("A. Basic Types:", font_size=36),
            Text("1. Undirected Graph", font_size=32),
            Text("2. Directed Graph (Digraph)", font_size=32)
        ).arrange(DOWN, aligned_edge=LEFT)
        
        types_B = VGroup(
            Text("B. Weight Types:", font_size=36),
            Text("1. Weighted Graphs", font_size=32),
            Text("2. Unweighted Graphs", font_size=32)
        ).arrange(DOWN, aligned_edge=LEFT)
        
        special_types = VGroup(
            Text("Special Graph Types:", font_size=36),
            Text("1. Trees", font_size=32),
            Text("2. Rooted Trees", font_size=32),
            Text("3. DAGs", font_size=32),
            Text("4. Bipartite Graphs", font_size=32),
            Text("5. Complete Graphs", font_size=32)
        ).arrange(DOWN, aligned_edge=LEFT)
        
        # Position the sections
        all_types = VGroup(types_A, types_B).arrange(RIGHT, buff=1)
        special_types.next_to(all_types, DOWN, buff=1)
        
        # Animation sequence
        self.play(Write(title))
        self.wait(0.5)
        self.play(FadeIn(types_A))
        self.wait(1)
        self.play(FadeIn(types_B))
        self.wait(1)
        self.play(FadeIn(special_types))
        self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects])

class GraphRepresentationScene(Scene):
    def construct(self):
        title = Text("Representing Graphs", font_size=48).to_edge(UP)
        
        # Example graph for all representations
        vertices = [Dot(point) for point in [LEFT*2, RIGHT*2, UP*2, DOWN*2]]
        edges = [
            Line(vertices[i].get_center(), vertices[j].get_center())
            for i, j in [(0,1), (1,2), (2,3), (3,0)]
        ]
        graph = VGroup(*vertices, *edges)
        
        # Matrix representation
        matrix = [
            [0, 1, 0, 1],
            [1, 0, 1, 0],
            [0, 1, 0, 1],
            [1, 0, 1, 0]
        ]
        matrix_mob = Matrix(matrix)
        matrix_label = Text("Adjacency Matrix", font_size=32)
        matrix_group = VGroup(matrix_label, matrix_mob).arrange(DOWN)
        
        # Adjacency list representation
        adj_list = VGroup(
            Text("1: [2, 4]", font_size=24),
            Text("2: [1, 3]", font_size=24),
            Text("3: [2, 4]", font_size=24),
            Text("4: [1, 3]", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT)
        adj_list_label = Text("Adjacency List", font_size=32)
        adj_list_group = VGroup(adj_list_label, adj_list).arrange(DOWN)
        
        # Edge list representation
        edge_list = Text("[(1,2), (2,3), (3,4), (4,1)]", font_size=24)
        edge_list_label = Text("Edge List", font_size=32)
        edge_list_group = VGroup(edge_list_label, edge_list).arrange(DOWN)
        
        # Position all representations
        representations = VGroup(
            matrix_group, adj_list_group, edge_list_group
        ).arrange(RIGHT, buff=1)
        representations.next_to(title, DOWN, buff=1)
        
        # Animation sequence
        self.play(Write(title))
        self.wait(0.5)
        self.play(Create(graph))
        self.wait(1)
        self.play(
            graph.animate.scale(0.5).to_corner(UL)
        )
        self.play(Write(matrix_group))
        self.wait(1)
        self.play(Write(adj_list_group))
        self.wait(1)
        self.play(Write(edge_list_group))
        self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects])

class GraphBasics(Scene):
    def construct(self):
        # Title and definition
        title = Text("Graph Theory Basics", font_size=48)
        definition = Text(
            "Graph theory is the mathematical theory of networks",
            font_size=32
        ).set_color(YELLOW)
        
        # Create social network example
        social_vertices = [
            Dot(point, color=BLUE) for point in [
                LEFT*3 + UP*1.5, RIGHT*3 + UP*1.5,
                LEFT*1.5, RIGHT*1.5,
                LEFT*3 + DOWN*1.5, RIGHT*3 + DOWN*1.5,
            ]
        ]
        
        # Add person icons (using simple circles with stick figures)
        person_icons = VGroup(*[
            VGroup(
                Circle(radius=0.2, color=BLUE),
                Line(start=DOWN*0.2, end=DOWN*0.6, color=BLUE)
            ).move_to(vertex.get_center())
            for vertex in social_vertices
        ])
        
        # Create edges for social network
        social_edges = [
            Line(
                social_vertices[i].get_center(),
                social_vertices[j].get_center(),
                color=WHITE
            )
            for i, j in [(0,1), (1,2), (2,3), (3,4), (4,5), (0,2), (1,3)]
        ]
        
        social_network = VGroup(*social_edges, *person_icons)
        
        # Create clothing graph example (simplified version)
        clothing_text = Text(
            "Real World Example: Clothing Combinations",
            font_size=24
        )
        
        clothing_vertices = [
            Dot(point) for point in [
                LEFT*4 + UP, LEFT*4 + DOWN,  # hats
                UP, DOWN,                    # shirts
                RIGHT*4 + UP, RIGHT*4 + DOWN # pants
            ]
        ]
        
        clothing_labels = [
            Text(label, font_size=20).next_to(vertex, direction)
            for vertex, label, direction in [
                (clothing_vertices[0], "Hats", LEFT),
                (clothing_vertices[2], "Shirts", UP),
                (clothing_vertices[4], "Pants", RIGHT)
            ]
        ]
        
        clothing_edges = [
            Arrow(
                clothing_vertices[i].get_center(),
                clothing_vertices[j].get_center(),
                buff=0.1
            )
            for i, j in [(0,2), (1,2), (2,4), (2,5)]
        ]
        
        clothing_graph = VGroup(
            *clothing_vertices,
            *clothing_edges,
            *clothing_labels
        )
        
        # Animation sequence
        self.play(Write(title))
        self.wait(0.5)
        
        # Move title up and show definition
        self.play(
            title.animate.to_edge(UP),
            Write(definition.next_to(title, DOWN))
        )
        self.wait()
        
        # Show social network example and fade out text
        self.play(
            Create(social_network),
            FadeOut(definition),
            FadeOut(title)
        )
        self.wait(2)
        
        # Transition to clothing graph
        self.play(
            FadeOut(social_network),
            Write(clothing_text.to_edge(UP))
        )
        self.play(Create(clothing_graph))
        self.wait(1)
        
        # Fade out clothing example
        self.play(
            FadeOut(clothing_text),
            FadeOut(clothing_graph)
        )
        self.wait(1)

class GraphTypes(Scene):
    def construct(self):
        # Title
        title = Text("Types of Graphs", font_size=48).to_edge(UP)
        
        # 1. Undirected Graph Example
        undirected_title = Text("Undirected Graph", font_size=36, color=YELLOW)
        
        # Create cities graph (A-F nodes with undirected edges)
        cities_vertices = {
            'A': Dot(LEFT*3 + DOWN, color=BLUE),
            'B': Dot(UP, color=BLUE),
            'C': Dot(LEFT*2 + DOWN*0.5, color=BLUE),
            'D': Dot(RIGHT + UP*0.5, color=BLUE),
            'E': Dot(RIGHT + DOWN, color=BLUE),
            'F': Dot(RIGHT*3, color=BLUE)
        }
        
        # Add labels to vertices
        city_labels = {
            key: Text(key, font_size=24).next_to(dot, UP*0.3)
            for key, dot in cities_vertices.items()
        }
        
        # Create undirected edges
        undirected_edges = [
            Line(cities_vertices[start].get_center(), 
                 cities_vertices[end].get_center())
            for start, end in [
                ('A','B'), ('B','C'), ('C','D'), ('D','E'),
                ('D','F'), ('B','D'), ('C','E')
            ]
        ]
        
        undirected_graph = VGroup(
            *cities_vertices.values(),
            *city_labels.values(),
            *undirected_edges
        )
        
        undirected_explanation = Text(
            "Cities connected by bidirectional roads",
            font_size=24
        ).next_to(undirected_graph, DOWN)
        
        # 2. Directed Graph Example
        directed_title = Text("Directed Graph (Digraph)", font_size=36, color=YELLOW)
        
        # Create gift-giving network
        directed_vertices = {
            'A': Dot(LEFT*2, color=BLUE),
            'B': Dot(UP + RIGHT, color=BLUE),
            'C': Dot(LEFT*2 + DOWN*2, color=BLUE),
            'D': Dot(RIGHT + DOWN, color=BLUE),
            'E': Dot(RIGHT*3, color=BLUE)
        }
        
        directed_labels = {
            key: Text(key, font_size=24).next_to(dot, UP*0.3)
            for key, dot in directed_vertices.items()
        }
        
        # Create directed edges with arrows
        directed_edges = [
            Arrow(directed_vertices[start].get_center(),
                 directed_vertices[end].get_center(),
                 buff=0.3)
            for start, end in [
                ('A','B'), ('B','E'), ('D','B'),
                ('B','D'), ('C','A'), ('D','C')
            ]
        ]
        
        directed_graph = VGroup(
            *directed_vertices.values(),
            *directed_labels.values(),
            *directed_edges
        )
        
        directed_explanation = Text(
            "Person u gave a gift to person v",
            font_size=24
        )
        
        # 3. Weighted Graph Example
        weighted_title = Text("Weighted Graph", font_size=36, color=YELLOW)
        
        # Create weighted network (reuse cities layout)
        weighted_vertices = {
            key: Dot(dot.get_center(), color=BLUE)
            for key, dot in cities_vertices.items()
        }
        
        weighted_labels = {
            key: Text(key, font_size=24).next_to(dot, UP*0.3)
            for key, dot in weighted_vertices.items()
        }
        
        # Create weighted edges with labels
        weighted_edges = []
        weights = [('A','B',4), ('B','C',8), ('C','D',3),
                  ('D','E',2), ('E','F',11), ('B','D',4),
                  ('C','E',9)]
        
        for start, end, weight in weights:
            edge = Line(
                weighted_vertices[start].get_center(),
                weighted_vertices[end].get_center()
            )
            weight_label = Text(
                str(weight),
                font_size=24
            ).next_to(edge.get_center(), UP, buff=0.1)
            weighted_edges.extend([edge, weight_label])
        
        weighted_graph = VGroup(
            *weighted_vertices.values(),
            *weighted_labels.values(),
            *weighted_edges
        )
        
        weighted_explanation = Text(
            "Edges represent distances/costs between nodes",
            font_size=24
        )
        
        # Animation sequence
        self.play(Write(title))
        self.wait(0.5)
        
        # Show undirected graph
        self.play(Write(undirected_title.next_to(title, DOWN)))
        self.play(Create(undirected_graph))
        self.play(Write(undirected_explanation))
        self.wait(2)
        self.play(
            FadeOut(undirected_graph),
            FadeOut(undirected_explanation),
            FadeOut(undirected_title)
        )
        
        # Show directed graph
        self.play(Write(directed_title.next_to(title, DOWN)))
        self.play(Create(directed_graph))
        self.play(Write(directed_explanation.next_to(directed_graph, DOWN)))
        self.wait(2)
        self.play(
            FadeOut(directed_graph),
            FadeOut(directed_explanation),
            FadeOut(directed_title)
        )
        
        # Show weighted graph
        self.play(Write(weighted_title.next_to(title, DOWN)))
        self.play(Create(weighted_graph))
        self.play(Write(weighted_explanation.next_to(weighted_graph, DOWN)))
        self.wait(2)
        
        # Final cleanup
        self.play(*[FadeOut(mob) for mob in self.mobjects])

class GraphProblems(Scene):
    def construct(self):
        # Create a graph for shortest path demonstration
        vertices = [
            Dot(point) for point in [
                LEFT*3, UP, RIGHT*3,
                DOWN*2 + LEFT, DOWN*2 + RIGHT
            ]
        ]
        edges = [
            Line(vertices[i].get_center(), vertices[j].get_center())
            for i, j in [(0,1), (1,2), (0,3), (3,4), (4,2)]
        ]
        graph = VGroup(*vertices, *edges)
        
        # Highlight shortest path
        path_edges = [edges[0], edges[1]]  # Example path
        highlighted_path = VGroup(*path_edges).copy().set_color(YELLOW)
        
        # Title and explanation
        title = Text("Common Graph Problems", font_size=40)
        subtitle = Text("Shortest Path", font_size=32)
        
        # Position elements
        title.to_edge(UP)
        subtitle.next_to(title, DOWN)
        graph.next_to(subtitle, DOWN, buff=1)
        
        # Animation sequence
        self.play(Write(title))
        self.play(Write(subtitle))
        self.play(Create(graph))
        self.wait()
        self.play(Create(highlighted_path))
        self.wait(2)

class ShortestPathAlgorithms(Scene):
    def construct(self):
        title = Text("Shortest Path Algorithms", font_size=48).to_edge(UP)
        
        # Create a weighted graph for demonstration
        vertices = [Dot(point) for point in [
            LEFT*4, LEFT*2, ORIGIN, RIGHT*2, RIGHT*4,
            DOWN*2 + LEFT*3, DOWN*2 + RIGHT*3
        ]]
        
        edges = []
        weights = [(0,1,4), (1,2,3), (2,3,2), (3,4,1),
                  (0,5,2), (5,6,5), (6,4,3), (1,6,6)]
        
        for start, end, weight in weights:
            edge = Line(vertices[start].get_center(), vertices[end].get_center())
            weight_label = Text(str(weight), font_size=24).next_to(edge.get_center(), UP, buff=0.1)
            edges.extend([edge, weight_label])
        
        graph = VGroup(*vertices, *edges)
        
        # Algorithms list
        algorithms = VGroup(
            Text("• BFS (unweighted)", font_size=32, color=BLUE),
            Text("• Dijkstra's Algorithm", font_size=32, color=GREEN),
            Text("• Bellman-Ford", font_size=32, color=RED),
            Text("• Floyd-Warshall", font_size=32, color=YELLOW),
            Text("• A* Algorithm", font_size=32, color=PURPLE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        
        # Animation sequence
        self.play(Write(title))
        self.play(Create(graph))
        self.wait(1)
        
        # Move graph to side and show algorithms
        self.play(
            graph.animate.scale(0.7).to_edge(LEFT),
            LaggedStartMap(FadeIn, algorithms.to_edge(RIGHT), lag_ratio=0.3)
        )
        self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects])

class ConnectivityAndFlow(Scene):
    def construct(self):
        title = Text("Network Flow & Connectivity", font_size=48).to_edge(UP)
        
        # Create a flow network
        source = Dot(LEFT*4, color=GREEN)
        sink = Dot(RIGHT*4, color=RED)
        mid_vertices = [Dot(point) for point in [LEFT*2, RIGHT*2, UP*2, DOWN*2]]
        
        # Create edges with capacities
        edges = []
        flow_values = [(source, mid_vertices[0], "5/10"),
                      (source, mid_vertices[2], "3/7"),
                      (mid_vertices[0], mid_vertices[1], "4/8"),
                      (mid_vertices[2], mid_vertices[1], "2/4"),
                      (mid_vertices[1], sink, "6/12")]
        
        for start, end, capacity in flow_values:
            arrow = Arrow(start.get_center(), end.get_center(), buff=0.3)
            cap_label = Text(capacity, font_size=24).next_to(arrow, UP, buff=0.1)
            edges.extend([arrow, cap_label])
        
        network = VGroup(source, sink, *mid_vertices, *edges)
        
        # Topics to cover
        topics = VGroup(
            Text("Maximum Flow:", font_size=36),
            Text("• Ford-Fulkerson Algorithm", font_size=28),
            Text("• Edmonds-Karp Algorithm", font_size=28),
            Text("\nConnectivity:", font_size=36),
            Text("• Union-Find DS", font_size=28),
            Text("• Bridge Detection", font_size=28)
        ).arrange(DOWN, aligned_edge=LEFT)
        
        # Animation
        self.play(Write(title))
        self.play(Create(network))
        self.wait(1)
        self.play(
            network.animate.scale(0.7).to_edge(LEFT),
            Write(topics.to_edge(RIGHT))
        )
        self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects])

class RealWorldApplications(Scene):
    def construct(self):
        title = Text("Real World Applications", font_size=48).to_edge(UP)
        
        # Create application examples with icons and descriptions
        applications = VGroup(
            VGroup(
                Text("🗺️ Navigation", font_size=36),
                Text("Shortest path in road networks", font_size=24)
            ).arrange(DOWN),
            VGroup(
                Text("🌐 Social Networks", font_size=36),
                Text("Friend recommendations", font_size=24)
            ).arrange(DOWN),
            VGroup(
                Text("💻 Computer Networks", font_size=36),
                Text("Routing and bandwidth", font_size=24)
            ).arrange(DOWN),
            VGroup(
                Text("🏭 Supply Chain", font_size=36),
                Text("Resource allocation", font_size=24)
            ).arrange(DOWN)
        ).arrange(DOWN, buff=0.8, aligned_edge=LEFT)
        
        # Animation
        self.play(Write(title))
        self.wait(0.5)
        self.play(LaggedStartMap(FadeIn, applications, lag_ratio=0.4))
        self.wait(2)
        
        # Final message
        final_message = Text(
            "Graph Theory: A powerful tool for solving real-world problems",
            font_size=36,
            color=YELLOW
        ).to_edge(DOWN)
        
        self.play(Write(final_message))
        self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects])

class CompletePresentation(Scene):
    def construct(self):
        # Introduction
        IntroScene.construct(self)
        
        # Basic Concepts
        GraphBasics.construct(self)
        
        # Types of Graphs
        GraphTypesOverview.construct(self)
        
        # Graph Representation
        GraphRepresentationScene.construct(self)
        
        # Algorithms and Problems
        ShortestPathAlgorithms.construct(self)
        
        # Network Flow and Connectivity
        ConnectivityAndFlow.construct(self)
        
        # Real World Applications
        RealWorldApplications.construct(self) 
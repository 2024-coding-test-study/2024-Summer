package 전보;

import java.util.*;
import java.io.*;
public class hun {
    static class Node implements Comparable<Node> {
        int vertex; // 정점을 나타내는 인덱스
        int weight; // 해당 정점까지의 가중치

        public Node(int vertex, int weight) {
            this.vertex = vertex;
            this.weight = weight;
        }

        @Override
        public int compareTo(Node other) {
            return Integer.compare(this.weight, other.weight);
        }
    }

    public static void dijkstra(int start, List<List<Node>> graph, int[] distances) {
        PriorityQueue<Node> priorityQueue = new PriorityQueue<>();
        priorityQueue.add(new Node(start, 0));
        distances[start] = 0;

        while (!priorityQueue.isEmpty()) {
            Node currentNode = priorityQueue.poll(); // 가장 작은 가중치를 가진 정점을 꺼냄
            int currentVertex = currentNode.vertex; // 꺼낸 정점의 인덱스

            for (Node neighbor : graph.get(currentVertex)) {
                int newDist = distances[currentVertex] + neighbor.weight;
                if (newDist < distances[neighbor.vertex]) {
                    distances[neighbor.vertex] = newDist;
                    priorityQueue.add(new Node(neighbor.vertex, newDist));
                }
            }
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int numVertices = scanner.nextInt();
        int numEdges = scanner.nextInt();

        List<List<Node>> graph = new ArrayList<>();
        for (int i = 0; i < numVertices; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < numEdges; i++) {
            int u = scanner.nextInt();
            int v = scanner.nextInt();
            int weight = scanner.nextInt();
            graph.get(u).add(new Node(v, weight));
            graph.get(v).add(new Node(u, weight)); // 무방향 그래프인 경우
        }

        int startVertex = scanner.nextInt();
        int[] distances = new int[numVertices];
        Arrays.fill(distances, Integer.MAX_VALUE);

        dijkstra(startVertex, graph, distances);

        System.out.println("Shortest distances from vertex " + startVertex + ":");
        for (int i = 0; i < distances.length; i++) {
            System.out.println("Vertex " + i + " : " + distances[i]);
        }
        int maxDistance= 0;
        for(int i : distances){
            if(maxDistance<i){
                maxDistance = i;
            }
        }
    }
}

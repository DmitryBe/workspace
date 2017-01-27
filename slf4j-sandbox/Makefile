
build:
	sbt compile
	sbt pack

clean:
	sbt clean

start-es:
	docker run --name=es -d -p 9200:9200 -p 5601:5601 nshou/elasticsearch-kibana

start-grafana:
	docker run -v /etc/localtime:/etc/localtime:ro -p 80:80 -p 8125:8125/udp -p 8126:8126 -p 8083:8083 -p 8086:8086 -p 8084:8084 --name kamon-grafana-dashboard muuki88/grafana_graphite:latest

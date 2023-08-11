mkdir rocketmq-consumer
cd rocketmq-consumer

touch RocketMQConsumer.java MessageStore.java Main.java

<project>
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.example</groupId>
  <artifactId>rocketmq-consumer</artifactId>
  <version>1.0-SNAPSHOT</version>
  <dependencies>
    <dependency>
      <groupId>org.apache.rocketmq</groupId>
      <artifactId>rocketmq-client</artifactId>
      <version>4.3.0</version>
    </dependency>
  </dependencies>
</project>

mvn compile
mvn exec:java -Dexec.mainClass="Main"

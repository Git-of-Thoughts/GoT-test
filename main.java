public class Main {
    public static void main(String[] args) {
        MessageStore messageStore = new MessageStore();
        RocketMQConsumer consumer = new RocketMQConsumer("consumerGroup1", "localhost:9876", messageStore);
        try {
            consumer.consume("TopicTest", "*");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

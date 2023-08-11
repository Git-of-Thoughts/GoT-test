import org.apache.rocketmq.client.consumer.DefaultMQPushConsumer;
import org.apache.rocketmq.common.message.MessageExt;

public class RocketMQConsumer {
    private DefaultMQPushConsumer consumer;
    private MessageStore messageStore;

    public RocketMQConsumer(String consumerGroup, String namesrvAddr, MessageStore messageStore) {
        this.consumer = new DefaultMQPushConsumer(consumerGroup);
        this.consumer.setNamesrvAddr(namesrvAddr);
        this.messageStore = messageStore;
    }

    public void consume(String topic, String tags) throws Exception {
        this.consumer.subscribe(topic, tags);
        this.consumer.registerMessageListener((List<MessageExt> msgs, ConsumeConcurrentlyContext context) -> {
            for (MessageExt msg : msgs) {
                processMessage(msg);
            }
            return ConsumeConcurrentlyStatus.CONSUME_SUCCESS;
        });
        this.consumer.start();
    }

    private void processMessage(MessageExt message) {
        String messageId = message.getMsgId();
        if (!this.messageStore.hasMessageId(messageId)) {
            // Process the message here
            // ...

            this.messageStore.addMessageId(messageId);
        }
    }
}

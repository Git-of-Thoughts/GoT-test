import java.util.HashSet;
import java.util.Set;

public class MessageStore {
    private Set<String> messageIds;

    public MessageStore() {
        this.messageIds = new HashSet<>();
    }

    public void addMessageId(String messageId) {
        this.messageIds.add(messageId);
    }

    public boolean hasMessageId(String messageId) {
        return this.messageIds.contains(messageId);
    }
}

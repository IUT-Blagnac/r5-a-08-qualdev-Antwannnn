package classes;

import java.util.ArrayList;
import java.util.List;

public class Order {

    private String owner;
    private String target;
    private String message;
    private final List<String> cocktails;

    public Order() {
        this.cocktails = new ArrayList<>();
    }

    public void declareOwner(String owner) {
        this.owner = owner;
    }

    public void declareTarget(String target) {
        this.target = target;
    }

    public void setMessage(String message) {
        this.message = message;
    }

    public String getTicket() {
        return String.format("From %s to %s: %s", owner, target, message);
    }

    public List<String> getCocktails() {
        return this.cocktails;
    }

    public void addCocktail(String s) {
        this.cocktails.add(s);
    }
}
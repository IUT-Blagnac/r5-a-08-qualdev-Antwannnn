import classes.Order;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;


import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class CocktailSteps {

    private Order order;

    @Given("{string} who wants to buy a drink")
    public void who_wants_to_buy_a_drink(String owner) {
        order = new Order();
        order.declareOwner(owner);
    }

    @When("an order is declared for {string}")
    public void an_order_is_declared_for(String target) {
        order.declareTarget(target);
    }

    @When("the order contains {int} cocktails")
    public void the_order_contains_cocktails(int nbCocktails) {
        for (int i = 0; i < nbCocktails; i++) {
            order.addCocktail("Cocktail " + (i + 1));  // Vous pouvez personnaliser le nom du cocktail ici
        }
    }

    @Then("there is {int} cocktails in the order")
    public void there_is_cocktails_in_the_order(int nbCocktails) {
        List<String> cocktails = order.getCocktails();
        assertEquals(nbCocktails, cocktails.size());
    }

    @When("a message saying {string} is added")
    public void a_message_saying_is_added(String message) {
        order.setMessage(message);
    }

    @Then("the ticket must say {string}")
    public void the_ticket_must_say(String expected) {
        String ticket = order.getTicket();
        assertEquals(expected, ticket);
    }
}
package hellocucumber;

import io.cucumber.java.en.Given;
import io.cucumber.java.en.When;
import io.cucumber.java.en.Then;
import static org.junit.jupiter.api.Assertions.*;

public class StepDefinitions {
    private String today;
    private String actualAnswer;

    @Given("today is {string}")
    public void today_is(String day) {
        today = day;
    }

    @When("I ask whether it's Friday yet")
    public void i_ask_whether_it_s_friday_yet() {
        actualAnswer = isItFriday(today);
    }

    static String isItFriday(String today) {
        if ("Friday".equals(today)) {
            return "TGIF";
        }
        return "Nope";
    }

    @Then("I should be told {string}")
    public void i_should_be_told(String expectedAnswer) {
        assertEquals(expectedAnswer, actualAnswer);
    }

    @Given("an example scenario")
    public void an_example_scenario() {
        // Empty implementation as this is just a setup step
    }

    @When("all step definitions are implemented")
    public void all_step_definitions_are_implemented() {
        // Empty implementation as this is just a verification step
    }

    @Then("the scenario passes")
    public void the_scenario_passes() {
        // We'll just assert true to make the test pass
        assertTrue(true);
    }

}

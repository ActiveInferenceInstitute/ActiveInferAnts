class LeNewConsumer:
    def __init__(self):
        self.values = {
            "optimism": "First and foremost, le new consumer is an optimist. “Over long time frames, the pessimist becomes an unobservant man, and the optimist creates the world,” wrote Simon Sarris. We are aware that the way we buy creates the world. And we are happy to spend money in a way that makes the world more like how we want it.",
            "empowerment": "Le new consumer believes in empowerment. We gather to give each other, collectively, more power. We don’t want to be manipulated. Many forces are at play in this rampant consumerism. We are breaking free. We exercise agency. We spot what’s wrong, manifest resourcefulness to build a better alternative, are not afraid to start from zero, and embody a growth mindset.",
            "balance": "Le new consumer strives for balance. We all face paradoxes. We all want one thing and its counterpart: home and adventure. Every system — including our own mind and body — flourishes between stability and change. New consumers accept this in themselves, and in others. We constantly look to reconcile: who we think we are, who we truly are, and who we aspire to become. This is how we feel at peace.",
            "intellectual_honesty": "Le new consumer values intellectual honesty above all. We don’t lie to ourselves. We know it’s hard. We are actually the easiest person to fool. But we avoid this at all costs. Not lying to yourself is the cornerstone of a more intentional life.",
            "relationships": "Le new consumer nurtures relationships. We reject the myth of ‘the more I buy the happier I’ll become’. We buy less and we buy better. We buy intentionally. Venkatesh Rao guided us: “You have to put more thinking into every act of ownership. (…) It isn’t the quantity of stuff in your life that matters. What matters is how smart the stuff is and whether it is smart in service of your needs.” We discard the old paradigm of ‘take, dispose and repeat’. We care instead. We are in a relationship with the objects in our life. “The quality of life is determined by the quality of our relationships,” says Esther Perel.",
            "questioning_intentions": "Le new consumer constantly questions the intentions at play. Which is why we worship that space between inception and action. New consumers know that their decision-making skill is exercising right in this space. We don’t rush it. We don’t drag it out either. We dance. We wonder. We imagine. Exactly in that space lies an erotic tension. We believe meaningful things are worth waiting for. New consumers don’t half-buy. 100% is what creates strong connections. Soulful connections give rise to enchantment.",
            "curation": "Le new consumer curates. We know why we did it. We say something with what we own. We celebrate connoisseurship. We are driven by infinite curiosity. We value craftsmanship. We believe in the beauty of the hand-crafted, home-made, community-inspired knowledge. We are also in awe with the level of ingenuity and perfection at which some big industries operate. Never before have humans perfected techniques and invented machines to be used at such a global scale. This demonstrates how impactful we can collectively be.",
            "embracing_friction": "Le new consumer embraces friction and boundaries. We treat objects like tattoos. You can’t get tattooed beyond your available skin. And this natural boundary is what makes tattoos feel special. New consumers joyfully adopt the same mindset with their consumption. It forces us to make choices. Those choices define us. And that’s what’s beautiful about them. We’re not scared of the word ‘enough’.",
            "producing_meaning": "Le new consumer produces meaning. Humans live and learn by stories. Objects are evidence of human existence. We are aware of the eternal. We imbue our objects with the sublime. “If you died tomorrow, what room full of stuff with your name on it would you like to leave behind?” asks Thom Bettridge. New consumers apply this to their home and surroundings.",
            "seeking_others": "Le new consumer seeks out other new consumers. That’s what made Sapiens singular in the first place. We only truly become someone when in relationship with others. We don’t lock meaningful objects inside vaults, we share them and celebrate them together. We believe in collective intelligence. We believe our rationales — why we have decided to nurture these specific possessions — can serve the public. We believe the stories and meaning of our objects should have a net positive effect on society."
        }

    def get_manifesto(self) -> str:
        manifesto = "manifesto\n"
        for key, value in self.values.items():
            manifesto += f"{value}\n\n"
        manifesto += "“Tell me, what is it you plan to do with your one wild and precious life?” — Mary Oliver\n"
        return manifesto

    def display_manifesto(self) -> None:
        print(self.get_manifesto())

    def apply_value(self, value_key: str) -> str:
        if value_key in self.values:
            return self.values[value_key]
        else:
            return "Value not found."

    def list_values(self) -> None:
        for key in self.values:
            print(f"{key}: {self.values[key]}")

    def operationalize_optimism(self) -> None:
        print("Operationalizing optimism: Focus on positive outcomes, set optimistic goals, and take actions that align with creating a better world.")

    def operationalize_empowerment(self) -> None:
        print("Operationalizing empowerment: Encourage collective power, exercise agency, and build resourceful alternatives to existing consumerism.")

    def operationalize_balance(self) -> None:
        print("Operationalizing balance: Strive for stability and change, reconcile personal paradoxes, and seek peace through self-acceptance.")

    def operationalize_intellectual_honesty(self) -> None:
        print("Operationalizing intellectual honesty: Avoid self-deception, embrace the difficulty of truth, and live intentionally.")

    def operationalize_relationships(self) -> None:
        print("Operationalizing relationships: Buy less but better, foster meaningful connections with objects, and prioritize the quality of relationships.")

    def operationalize_questioning_intentions(self) -> None:
        print("Operationalizing questioning intentions: Reflect on decision-making, embrace the space between inception and action, and seek soulful connections.")

    def operationalize_curation(self) -> None:
        print("Operationalizing curation: Celebrate craftsmanship, value ingenuity, and make intentional choices about ownership.")

    def operationalize_embracing_friction(self) -> None:
        print("Operationalizing embracing friction: Accept natural boundaries, make choices that define you, and find beauty in the concept of 'enough'.")

    def operationalize_producing_meaning(self) -> None:
        print("Operationalizing producing meaning: Imbue objects with stories, recognize the eternal, and create a meaningful environment.")

    def operationalize_seeking_others(self) -> None:
        print("Operationalizing seeking others: Share meaningful objects, celebrate collective intelligence, and contribute positively to society.")

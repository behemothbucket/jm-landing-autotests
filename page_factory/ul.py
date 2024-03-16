from page_factory.component import Component


class Ul(Component):
    @property
    def type_of(self) -> str:
        return "Ul"

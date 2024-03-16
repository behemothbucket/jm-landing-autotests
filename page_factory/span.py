from page_factory.component import Component


class Span(Component):
    @property
    def type_of(self) -> str:
        return "span"

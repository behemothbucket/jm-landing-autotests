from page_factory.component import Component


class Checkbox(Component):
    @property
    def type_of(self) -> str:
        return "checkbox"

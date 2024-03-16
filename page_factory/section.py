from page_factory.component import Component


class Section(Component):
    @property
    def type_of(self) -> str:
        return "Section"

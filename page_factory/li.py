from page_factory.component import Component


class Li(Component):
    @property
    def type_of(self) -> str:
        return "Li"

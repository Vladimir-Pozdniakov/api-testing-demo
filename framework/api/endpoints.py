class AuthorAPI:
    """Endpoints for Author API"""

    base = "/author"

    @staticmethod
    def by_name(name: str) -> str:
        """Get author by name endpoint"""
        return f"/author/{name}"


class TitleAPI:
    """Endpoints for Title API"""

    base = "/title"

    @staticmethod
    def by_name(name: str) -> str:
        """Get title by name endpoint"""
        return f"/title/{name}"


class RandomAPI:
    """Endpoints for Random API"""

    base = "/random"


class LinesAPI:
    """Endpoints for Lines API"""

    @staticmethod
    def by_line_text(text: str) -> str:
        """Get lines by number endpoint"""
        return f"/lines/{text}"

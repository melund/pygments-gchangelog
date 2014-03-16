from .utils import TestCase
import pygments_gchangelog
import pygments.lexers
import pygments.styles


CHANGELOG_TEST1 = """\
#  Comment

  12 Mar 2014; John Doe <john@doe.com> some-1.0.0-r1.ebuild:
  Fix bug #10000

*some-1.0.0-r1 (19 Jan 2014)

  19 Jan 2014; John Doe <john@doe.com> +some-1.0.0-r1.ebuild:
  Revbump for last change.

"""


class ChangelogTest(TestCase):

    def test_install_lexer(self):
        lexer1 = pygments.lexers.get_lexer_by_name('changelog')
        self.assertIsInstance(lexer1, pygments_gchangelog.ChangelogLexer)
        style = pygments.styles.get_style_by_name('changelog')
        self.assertIs(style, pygments_gchangelog.ChangelogStyle)

    def test_lexer(self):
        lexer = pygments_gchangelog.ChangelogLexer()
        tokens = list(lexer.get_tokens(CHANGELOG_TEST1))
        self.assertIn(tokens[0][0], pygments_gchangelog.Comment)
        self.assertEqual(tokens[0][1], "#  Comment\n")
        self.assertEqual(tokens[3][0], pygments_gchangelog.Date)
        self.assertEqual(tokens[3][1], "12 Mar 2014")
        self.assertIn(
            (pygments_gchangelog.File, "some-1.0.0-r1.ebuild"),
            tokens
        )
        self.assertIn((pygments_gchangelog.Date, "19 Jan 2014"), tokens)
